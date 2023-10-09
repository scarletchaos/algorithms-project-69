import pytest
from search_engine.search_engine import search
from search_engine.search_engine import reverse_index
from search_engine.search_engine import tf_idf


@pytest.fixture
def data():
    doc1 = "I can't shoot shoot shoot shoot shoot shoot shoot shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    # создание документа
    # документ имеет два атрибута "id" и "text"
    return [
        {"id": "doc1", "text": doc1},
        {"id": "doc2", "text": doc2},
        {"id": "doc3", "text": doc3},
    ]


def test_search(data):
    assert search(data, "shoot") in [["doc1", "doc2"], ["doc2", "doc1"]]


def test_search_empty():
    assert search([], "shoot") == []


def test_search_extra_symbols(data):
    assert search(data, "pint") == ["doc1"]
    assert search(data, "pint!") == ["doc1"]


def test_search_relevancy(data):
    assert search(data, "shoot") == ["doc1", "doc2"]


def test_fuzzy_search(data):
    assert search(data, "shoot at me") == ["doc2", "doc1"]


def test_reverse_index():
    doc1 = "Some data"
    doc2 = "Some more data"
    doc3 = "Even more"
    docs = [
        {"id": "doc1", "text": doc1},
        {"id": "doc2", "text": doc2},
        {"id": "doc3", "text": doc3},
    ]

    assert reverse_index(docs) == {
        "some": ["doc1", "doc2"],
        "more": ["doc2", "doc3"],
        "data": ["doc1", "doc2"],
        "even": ["doc3"],
    }


def test_tfidf(data):
    print(tf_idf(data, data[0], "shoot"))
    assert tf_idf(data, data[0], "shoot") > tf_idf(data, data[1], "shoot")
