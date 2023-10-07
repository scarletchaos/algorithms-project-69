from typing import Optional


def search(docs: list[Optional[dict[str, str]]], query: str) -> list[Optional[str]]:
    result = []
    for doc in docs:
        if query in doc["text"].split(' '):
            result.append(doc["id"])
    return result
