# -*- coding: utf-8 -*-
"""
用 huggingface 的 module 做一些 bert pre train model 的试验性代码

需要试验的内容：
1) 英文版的 bert（tf2 version） 以及一些 fine tuning task
2) 中文版的 bert
"""

import tensorflow as tf
from gs_framework.gs_resource import set_http_proxy
from transformers import BertTokenizer, TFBertForSequenceClassification, TFBertForPreTraining, AutoTokenizer, \
    AutoModelWithLMHead, TFAutoModelWithLMHead, TFAutoModel

set_http_proxy()


def run_first_test():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')
    input_ids = tf.constant(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True))[None, :]  # Batch size 1
    print(f"input_ids:{input_ids}")
    outputs = model(input_ids)
    logits = outputs[0]
    print(logits)
    print("-" * 30)
    print(f"outputs:{outputs}")
    print("-" * 30)
    model.summary()


def run_chinese_bert():
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
    model = TFBertForPreTraining.from_pretrained('bert-base-chinese', output_attentions=True)
    # print(f"model config:{model.config}")
    # model.config.output_attentions = True
    input_ids = tf.constant(tokenizer.encode("习近平总书记讲到三个关联“做好疫情防控工作，直接关系人民生命安全和身体健康，直接关系经济社会大局稳定，也事关我国对外开放”"))[None,:]  # Batch size 1

    outputs = model(input_ids)
    print(f"outputs shapes:{outputs}")
    logits = outputs[0]
    # print(logits)
    # print("-" * 30)
    # print(f"outputs:{outputs}")
    print("-" * 30)
    # print(tf.math.argmax(logits, axis=2)[0, :])
    print(tokenizer.decode(tf.math.argmax(logits, axis=2)[0, :]))
    # model.summary()


def run_chinese_bert_wwm_torch():
    import torch
    tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-bert-wwm-ext")
    model = AutoModelWithLMHead.from_pretrained("hfl/chinese-bert-wwm-ext")

    input_ids = torch.tensor(tokenizer.encode("[MASK][MASK][MASK]总书记讲到三个关联“做好[MASK][MASK]防控工作，直接关系[MASK][MASK]生命安全和身体健康，直接关系经济社会大局稳定，也事关我国对外开放”", add_special_tokens=True)).unsqueeze(
        0)  # Batch size 1
    # print(f"input_ids:{input_ids}")
    outputs = model(input_ids)
    logits = outputs[0]
    # print(logits)
    # print("-" * 30)
    # print(f"outputs:{outputs}")
    print("-" * 30)
    # print(tf.math.argmax(logits, axis=2)[0, :])
    print(tokenizer.decode(torch.argmax(logits, dim=2)[0, :]))

if __name__ == "__main__":
    # run_first_test()
    run_chinese_bert()
    # run_chinese_bert_wwm_torch()
