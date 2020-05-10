import pickle
import argparse
import sys
import os

from invested_index import InvestedIndex


docs_path = os.path.join(os.getcwd(), "investeddata")
index = InvestedIndex(docs_path=docs_path)


def get_result_with_nums(query, nums=5):
    keys = index.get_key_from_query(query)
    result = None
    for k in keys:
        if result is None:
            result = index.invested_index.get(k)
        else:
            result.intersection_update(index.invested_index.get(k))
    if len(result) >= nums:
        return list(result)[:nums]
    else:
        return list(result)

if __name__ == "__main__":
    text = """Thử nghiệm vũ khí hạt nhân"""
    print(get_result_with_nums(text, 3))