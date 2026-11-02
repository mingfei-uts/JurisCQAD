# JurisCQAD

[简体中文](README.md) | **English**

A cleaned Chinese legal question-answering dataset containing **43,104 records**.

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

## Cleaning scope

This version underwent de-identification, exact-record deduplication, screening of promotional and non-substantive answers, isolation of generation artifacts, and removal of explicit answer-label cues. The same leading-header cleanup rules were applied to both answer fields, while substantive legal expressions were preserved.

Quarantined records and audit logs containing removed text are not published.

## Usage notes

- Field names reflect the dataset's existing annotations; they do not imply that every answer has been verified for legal correctness.
- During evaluation, hide the original field names, use anonymous candidates in randomized order, and store labels separately.
- Keep identical or similar questions in the same partition when creating training and test sets to avoid leakage.
- Removing explicit cues does not eliminate all possible shortcuts based on writing style, length, or other features.
- The data is intended for research and should not be used as legal advice for individual cases.

## Integrity check

SHA-256 of the decompressed `JurisCQAD_cleaned.jsonl`:

```text
52f812c4fb3700740a97f78fb9b0119dbd982b05a6f63a4ff96e63d5495ff6b1
```
