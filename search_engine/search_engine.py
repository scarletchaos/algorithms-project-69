from typing import Optional
import re


def search(docs: list[Optional[dict[str, str]]], query: str) -> list[Optional[str]]:

    term = ''.join(re.findall(r'\w+', query)).lower()
    result = []
    for doc in docs:
        appearances = len(re.findall(f'(?<!\\w){term}(?!\\w)', doc['text'].lower()))
        if appearances:
            result.append([doc["id"], appearances])

    result.sort(key=lambda doc: doc[1], reverse=True)
    return [doc[0] for doc in result]   
