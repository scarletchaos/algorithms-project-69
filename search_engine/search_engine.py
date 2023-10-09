from math import log2
from typing import Optional
import re


def compare_texts(t1, t2):
    if t1[1] == t2[1]:
        if t1[2] > t2[2]:
            return 1
        elif t1[2] < t2[2]:
            return -1
        else:
            return 0
    elif t1[1] > t2[1]:
        return 1
    else:
        return -1


def search(
    docs: list[Optional[dict[str, str]]], query: str
) -> list[Optional[str]]:
    terms = re.findall(r"\w+", query)
    print(terms)
    result = []
    for doc in docs:
        appears_total = 0
        wordcount = 0
        tfidf = 0
        for term in terms:
            appears = len(
                re.findall(f"(?<!\\w){term}(?!\\w)", doc["text"].lower())
            )
            tfidf += tf_idf(docs, doc, term)
            if appears:
                wordcount += 1
                appears_total += appears
        if wordcount or appears_total:
            result.append([doc["id"], wordcount, appears_total, tfidf])

    result.sort(key=lambda x: x[3], reverse=True)
    print(result)
    return [doc[0] for doc in result]


def reverse_index(docs: list[Optional[dict[str, str]]]) -> dict[str, list[str]]:
    result = {}
    for doc in docs:
        words = re.findall(r"\w+", doc["text"].lower())
        for word in words:
            if word not in result.keys():
                result[word] = [doc["id"]]
            else:
                if doc["id"] not in result[word]:
                    result[word].append(doc["id"])

    return result


def tf_idf(
    docs: list[Optional[dict[str, str]]], doc: dict[str, str], query: str
) -> float:
    rev = reverse_index(docs)
    term = "".join(re.findall(r"\w+", query))

    term_count = len(re.findall(f"(?<!\\w){term}(?!\\w)", doc["text"].lower()))
    tf = term_count / len(doc["text"].split(" "))

    idf = log2(
        (1 + (len(docs) - (len(rev[term]) if term in rev.keys() 
                                          else 0) + 1) / ((len(rev[term]) if
                                                           term in rev.keys()
                                                           else 0) + 0.5)
        )
    )
    return tf * idf
