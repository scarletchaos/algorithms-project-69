import pytest
from search_engine.search_engine import search


@pytest.fixture
def data():
    doc1 = "I can't shoot straight unless I've had a pint!"
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
    assert search(data, "shoot") in [["doc1", "doc2"],  ["doc2", "doc1"]]


def test_search_empty():
    assert search([], "shoot") == []


def test_search_extra_symbols(data):
    assert search(data, "pint") == ["doc1"]
    assert search(data, "pint!") == ["doc1"]

def test_search_relevancy():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {"id": "doc1", "text": doc1},
        {"id": "doc2", "text": doc2},
        {"id": "doc3", "text": doc3},
    ]
    assert search(docs, 'shoot') == ['doc2', 'doc1']
