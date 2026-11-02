# JurisCQAD

[English](README.md) | **简体中文**

本仓库提供我们论文 [**From Query to Counsel: Structured Reasoning with a Multi-Agent Framework and Dataset for Legal Consultation**](https://aclanthology.org/2026.acl-long.776/) 的数据集 **JurisCQAD**。我们的论文已被 **ACL 2026 接收为 Oral（口头报告）**。

JurisCQAD 是一个中文法律咨询问答数据集，当前发布版本包含 **43,104 条记录**。

## 数据文件

[JurisCQAD_cleaned.jsonl.gz](JurisCQAD_cleaned.jsonl.gz) 为 gzip 无损压缩文件。解压后是 UTF-8 编码的 JSON Lines 文件，每行一个 JSON 对象，包含以下字段：

| 字段 | 含义 |
| --- | --- |
| `问题内容` | 问题文本 |
| `原答案` | 数据集中标注的原答案 |
| `错误答案` | 数据集中标注的错误答案 |

## 读取方式

下载数据文件后，使用 Python 标准库直接读取，无需预先解压：

```python
import gzip
import json

with gzip.open("JurisCQAD_cleaned.jsonl.gz", "rt", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line)
        question = record["问题内容"]
        original_answer = record["原答案"]
        incorrect_answer = record["错误答案"]
```

## 完整性校验

解压后 `JurisCQAD_cleaned.jsonl` 的 SHA-256：

```text
52f812c4fb3700740a97f78fb9b0119dbd982b05a6f63a4ff96e63d5495ff6b1
```

## 引用

如果你在研究中使用 JurisCQAD，请引用：

```bibtex
@inproceedings{lu-etal-2026-query,
    title = "From Query to Counsel: Structured Reasoning with a Multi-Agent Framework and Dataset for Legal Consultation",
    author = "Lu, Mingfei  and
      Zhang, Yi  and
      Wu, Mengjia  and
      Feng, Yue",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.776/",
    doi = "10.18653/v1/2026.acl-long.776",
    pages = "17064--17078",
    ISBN = "979-8-89176-390-6",
    abstract = "Legal consultation question answering (Legal CQA) presents unique challenges compared to traditional legal QA tasks, including the scarcity of high-quality training data, complex task composition, and strong contextual dependencies. To address these, we construct JurisCQAD, a large-scale dataset of over 43,000 real-world Chinese legal queries annotated with expert-validated positive and negative responses, and design a structured task decomposition that converts each query into a legal element graph integrating entities, events, intents, and legal issues. We further propose JurisMA, a modular multi-agent framework supporting dynamic routing, statutory grounding, and stylistic optimization. Combined with the element graph, the framework enables strong context-aware reasoning, effectively capturing dependencies across legal facts, norms, and procedural logic. Trained on JurisCQAD and evaluated on a refined LawBench, our system significantly outperforms both general-purpose and legal-domain LLMs across multiple lexical and semantic metrics, demonstrating the benefits of interpretable decomposition and modular collaboration in Legal CQA."
}
```
