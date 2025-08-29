/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

# Licensed under the MIT License
"""
Reference:
 - [LightRag](https://github.com/HKUDS/LightRAG)
 - [MiniRAG](https://github.com/HKUDS/MiniRAG)
"""
PROMPTS = {}

PROMPTS["minirag_query2kwd"] = """---Role---

You are a helpful assistant tasked with identifying both answer-type and low-level keywords in the user's query.

---Goal---

Given the query, list both answer-type and low-level keywords.
