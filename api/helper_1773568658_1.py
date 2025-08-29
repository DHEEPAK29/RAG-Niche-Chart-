/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

from common.metadata_utils import meta_filter


def test_contains():
    # returns chunk where the metadata contains the value
    metas = {"version": {"hello earth": ["doc1"], "hello mars": ["doc2"]}}
    filters = [{"key": "version", "op": "contains", "value": "earth"}]

    assert meta_filter(metas, filters) == ["doc1"]


def test_not_contains():
    # returns chunk where the metadata does not contain the value
    metas = {"version": {"hello earth": ["doc1"], "hello mars": ["doc2"]}}
    filters = [{"key": "version", "op": "not contains", "value": "earth"}]
