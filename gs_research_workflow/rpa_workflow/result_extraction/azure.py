# -*- coding: UTF-8 -*-
import glob
import os
from typing import Optional, Dict, List, Any

from mongoengine import Document

from gs_research_workflow.nlp.data.docs_in_mongo import AzureTextAna, Sentiment, EntityInDoc, GlobalEntityLinking, \
    GlobalEntity, Article, UserInTwitter
from gs_research_workflow.rpa_workflow.result_extraction.utilities import upsert_document
import logging
logger = logging.getLogger(__name__)


class AzureDataProcess:

    @staticmethod
    def sentiment2int(s) -> Optional[int]:
        if s == "positive":
            return 1
        elif s == "neutral":
            return 0
        elif s == "negative":
            return -1
        else:
            return None

    @staticmethod
    def str_2_azure_txt_ana(s: str, batch_action_uuid: str, action_uuid: str, save_doc: bool) -> AzureTextAna:
        import json
        ana_dict = json.loads(s)

        def read_tree_dict(v: Dict, key_path: List[str], default_val: Any) -> Any:
            curr_step = v
            for k in key_path:
                if k == ":first":  # 特殊的 key ，用于得到 list 的第一个对象，目前的场景够用了
                    assert isinstance(curr_step, list)
                    if len(curr_step) == 0 :
                        curr_step = None
                    else:
                        curr_step = curr_step[0]
                else:
                    curr_step = curr_step.get(k, None)
                if curr_step is None:
                    return default_val
            return curr_step
        rlt_ana = AzureTextAna()
        rlt_ana.detected_language = read_tree_dict(ana_dict,
                                                   ["languageDetection", "documents", ":first", "detectedLanguages",
                                                    ":first", "iso6391Name"], None)
        rlt_ana.detected_language_score = read_tree_dict(ana_dict,
                                                         ["languageDetection", "documents", ":first",
                                                          "detectedLanguages",
                                                          ":first", "score"], None)
        rlt_ana.key_phrases = read_tree_dict(ana_dict, ["keyPhrases", "documents", ":first",
                                                        "keyPhrases"], None)
        rlt_ana.doc_sentiment = Sentiment(
            sentiment=AzureDataProcess.sentiment2int(read_tree_dict(ana_dict, ["sentiment", "documents", ":first", "sentiment"], None)),
            positive_score=read_tree_dict(ana_dict, ["sentiment", "documents", ":first", "documentscores",
                                                     "positive"], None),
            neutral_score=read_tree_dict(ana_dict, ["sentiment", "documents", ":first", "documentscores",
                                                     "neutral"], None),
            negative_score=read_tree_dict(ana_dict, ["sentiment", "documents", ":first", "documentscores",
                                                    "negative"], None),
        )
        ls_sentences_sentiment: List[Sentiment] = list()
        it_v = read_tree_dict(ana_dict, ["sentiment", "documents", ":first", "sentences"], None)
        if it_v :
            for curr_v in it_v:
                curr_sentences_sentiment = Sentiment(
                    sentiment=AzureDataProcess.sentiment2int(read_tree_dict(curr_v, ["sentiment"], None)),
                    positive_score=read_tree_dict(curr_v, ["sentencescores", "positive"], None),
                    neutral_score=read_tree_dict(curr_v, ["sentencescores", "neutral"], None),
                    negative_score=read_tree_dict(curr_v, ["sentencescores", "negative"], None),
                    offset=read_tree_dict(curr_v, ["offset"], None),
                    length=read_tree_dict(curr_v, ["length"], None),
                )
                ls_sentences_sentiment.append(curr_sentences_sentiment)
            rlt_ana.sentences_sentiment = ls_sentences_sentiment

        ls_entities: List[EntityInDoc] = list()
        it_v = read_tree_dict(ana_dict, ["entities", "documents", ":first", "entities"], None)
        if it_v:
            for curr_v in it_v:
                curr_entity = EntityInDoc(
                    text=read_tree_dict(curr_v, ["text"], None),
                    type=read_tree_dict(curr_v, ["type"], None),
                    subtype=read_tree_dict(curr_v, ["subtype"], None),
                    offset=read_tree_dict(curr_v, ["offset"], None),
                    length=read_tree_dict(curr_v, ["length"], None),
                    score=read_tree_dict(curr_v, ["score"], None)
                )
                ls_entities.append(curr_entity)
            rlt_ana.entities = ls_entities

        ls_entity_linking: List[GlobalEntityLinking] = list()
        it_v = read_tree_dict(ana_dict, ["entityLinking", "documents", ":first", "entities"], None)
        if it_v:
            for curr_v in it_v:
                entity_id = read_tree_dict(curr_v, ["id"], None)
                if entity_id is None:  # 发现会出现 entity id 为 None 的情况出现而引起错误
                    continue
                g_entity = GlobalEntity(
                    entity_id=entity_id,
                    name=read_tree_dict(curr_v, ["name"], None),
                    language=read_tree_dict(curr_v, ["language"], None),
                    url=read_tree_dict(curr_v, ["url"], None),
                    data_source=read_tree_dict(curr_v, ["datasource"], None),
                    batch_action_uuid=batch_action_uuid
                )
                if save_doc:
                    upsert_document(g_entity, True)
                embedded_entity = GlobalEntityLinking(
                    entity=g_entity,
                    text=read_tree_dict(curr_v, ["matches", ":first", "text"], None),
                    offset=read_tree_dict(curr_v, ["matches", ":first", "offset"], None),
                    length=read_tree_dict(curr_v, ["matches", ":first", "length"], None),
                    score=read_tree_dict(curr_v, ["matches", ":first", "score"], None),
                )
                ls_entity_linking.append(embedded_entity)
            rlt_ana.entity_linking = ls_entity_linking

        ls_entity_pii: List[EntityInDoc] = list()
        it_v = read_tree_dict(ana_dict, ["entityPII", "documents", ":first", "entities"], None)
        if it_v:
            for curr_v in it_v:
                curr_entity = EntityInDoc(
                    text=read_tree_dict(curr_v, ["text"], None),
                    type=read_tree_dict(curr_v, ["type"], None),
                    subtype=read_tree_dict(curr_v, ["subtype"], None),
                    offset=read_tree_dict(curr_v, ["offset"], None),
                    length=read_tree_dict(curr_v, ["length"], None),
                    score=read_tree_dict(curr_v, ["score"], None)
                )
                ls_entity_pii.append(curr_entity)
            rlt_ana.entity_pii = ls_entity_pii

        return rlt_ana

    @staticmethod
    def txt_analyse(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> List[Document]:
        ls_rlt: List[Document] = list()
        import pickle
        # 暂时先hardcode，以后可以改成动态产生
        doc_cls_mapping = {"Article": Article, "UserInTwitter": UserInTwitter}
        rlt_files = glob.glob(os.path.join(rlt_path, "*.pkl"))
        if rlt_files:
            for i, f_name in enumerate(rlt_files):
                logger.info(f"proecess file : {f_name} ")
                with open(f_name, "rb") as f:
                    val: Dict = pickle.load(f)
                doc_cls = doc_cls_mapping[val["doc"]]
                pk_field_name = val["pk_field"]
                pk_val = val["pk_val"]
                txt_field = val["txt_field"]
                ana_rlt = AzureDataProcess.str_2_azure_txt_ana(val["ana_result"], batch_action_uuid, save_doc)

                dict_init = {pk_field_name: pk_val, f"{txt_field}_ana": ana_rlt}
                obj = doc_cls(**dict_init)
                if save_doc:
                    upsert_document(obj, True)
                ls_rlt.append(obj)
        return ls_rlt