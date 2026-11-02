# JurisCQAD

**简体中文** | [English](README.en.md)

清理后的中文法律问答数据集，共 **43,104 条记录**。

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

## 清理范围

本版本经过脱敏处理、完全重复记录去重、推广及无实质回答筛选、生成残留隔离，以及显式正误提示清理。两类答案采用相同的开头格式清理规则，保留“虚构事实”等属于法律正文的表述。

隔离记录及含删除前内容的审计日志未公开。

## 使用说明

- 字段名反映数据集原有标注，不代表每条答案都已通过法律正确性审定。
- 评测时应隐藏“原答案”和“错误答案”字段名，使用匿名候选并随机交换顺序，将标签单独保存。
- 划分训练集和测试集时，应将相同或近似问题放入同一分区，避免数据泄漏。
- 清理显式提示不代表消除了文风、长度等所有隐性线索。
- 数据用于研究，不应作为个案法律意见。

## 完整性校验

解压后 `JurisCQAD_cleaned.jsonl` 的 SHA-256：

```text
52f812c4fb3700740a97f78fb9b0119dbd982b05a6f63a4ff96e63d5495ff6b1
```
