from typing import Optional
import re
import functools


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


def search(docs: list[Optional[dict[str, str]]], query: str) -> list[Optional[str]]:
    terms = re.findall(r"\w+", query)
    print(terms)
    result = []
    for doc in docs:
        appears_total = 0
        wordcount = 0
        for term in terms:
            appears = len(re.findall(f"(?<!\\w){term}(?!\\w)", doc["text"].lower()))
            if appears:
                wordcount += 1
                appears_total += appears
        if wordcount or appears_total:
            result.append([doc["id"], wordcount, appears_total])

    result.sort(key=functools.cmp_to_key(compare_texts), reverse=True)
    print(result)
    return [doc[0] for doc in result]


def reverse_index(docs: list[Optional[dict[str, str]]]) -> dict[str, list[str]]:
    result = {}
    for doc in docs:
        words = re.findall(r"\w+", doc['text'].lower())
        for word in words:
            if word not in result.keys():
                result[word] = [doc['id']]
            else:
                result[word].append(doc['id'])

    return result

