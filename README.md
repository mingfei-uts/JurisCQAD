# JurisCQAD

**English** | [简体中文](README.zh-CN.md)

This repository contains **JurisCQAD**, the dataset for our paper [**From Query to Counsel: Structured Reasoning with a Multi-Agent Framework and Dataset for Legal Consultation**](https://aclanthology.org/2026.acl-long.776/), accepted to **ACL 2026 as an Oral presentation**.

JurisCQAD is a Chinese legal consultation question-answering dataset. This release contains **43,104 records**.

## Data file

[JurisCQAD_cleaned.jsonl.gz](JurisCQAD_cleaned.jsonl.gz) is a losslessly gzip-compressed file. After decompression, it is a UTF-8 JSON Lines file with one JSON object per line and the following fields:

| Field | Description |
| --- | --- |
| `问题内容` | Question text |
| `原答案` | Answer labeled as the original answer in the dataset |
| `错误答案` | Answer labeled as incorrect in the dataset |

## Reading the data

Download the data file and read it directly with the Python standard library. No prior decompression is required:

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

## Integrity check

SHA-256 of the decompressed `JurisCQAD_cleaned.jsonl`:

```text
52f812c4fb3700740a97f78fb9b0119dbd982b05a6f63a4ff96e63d5495ff6b1
```

## Citation

If you use JurisCQAD in your research, please cite:

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
