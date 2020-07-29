# -*- coding: UTF-8 -*-

from mongoengine import Document
import logging
logger = logging.getLogger(__name__)


def parse_num_from_str(s) -> float:
    if not isinstance(s, str):
        return s
    if not s:
        return None
    try:
        s = s.upper().replace(",", "")
        if s.endswith("K"):
            return float(s[0:-1]) * 1e3
        elif s.endswith("M"):
            return float(s[0:-1]) * 1e6
        elif s.endswith("G") or s.endswith("B"):
            return float(s[0:-1]) * 1e9
        elif s.endswith("T"):
            return float(s[0:-1]) * 1e12
        elif s.endswith("P"):
            return float(s[0:-1]) * 1e15
        else:
            return float(s)
    except ValueError as ex:
        logger.error(ex)
        return None


def append_site_to_url(url: str, site: str) -> str:
    if not url:
        return url
    if not isinstance(url, str):
        return url
    if url.lower().startswith("http:") or url.lower().startswith("https:"):
        return url
    if url.startswith("/"):
        return site + url
    elif url.startswith("./"):
        return site + url[1:]
    else:
        return site + "/" + url


def upsert_document(doc: Document, cascade: bool = True):
    dict_2_update = dict()
    for field in doc._fields_ordered:
        if getattr(doc, field, None) is not None:
            v = getattr(doc, field, None)
            dict_2_update[field] = v
            if isinstance(v, Document) and cascade:
                upsert_document(v, cascade)
    dict_2_update["upsert"] = True
    try:
        doc.update(**dict_2_update)
    except Exception as ex:
        logger.error(f"{doc.__class__}:{doc.to_json()}")
        raise ex