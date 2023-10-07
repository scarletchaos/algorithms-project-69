from typing import Optional
import re


def search(docs: list[Optional[dict[str, str]]], query: str) -> list[Optional[str]]:

    term = ''.join(re.findall(r'\w+', query)).lower()
    result = []
    for doc in docs:
        if re.findall(f'(?<!\\w){term}(?!\\w)', doc['text'].lower()):
            result.append(doc["id"])
    return result
