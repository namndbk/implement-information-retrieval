import re
import os
import pickle
import sys

import utils


class InvestedIndex(object):
    def __init__(self, docs_path=None):
        if docs_path is None:
            self.invested_index = {}
        else:
            self._load(docs_path)
            self.dictionary = self.invested_index.keys()
    

    def _assert_dir(self, docs_path):
        if not os.path.exists(docs_path):
            print("Error: {} does not exits.".format(docs_path))
            sys.exit(1)
        if not os.path.isdir(docs_path):
            print("Error: {} is not directory.".format(docs_path))
    

    def _get_text_from_file(self, filename):
        with open(filename, "rb") as f:
            text = f.read()
            text = text.decode("utf-16")
        return text
    

    def _get_word_from_text(self, text):
        words = utils.get_words(text)
        return words
    

    def build_invested_index(self, docs_path, mode="build"):
        if mode == "update":
            self._load("investeddata")
        self._assert_dir(docs_path)
        for doc_file in os.listdir(docs_path):
            filename = os.path.join(docs_path, doc_file)
            text = self._get_text_from_file(filename)
            words = self._get_word_from_text(text)


            for w in words:
                if self.invested_index.get(w) is None:
                    self.invested_index[w] = {doc_file}
                else:
                    self.invested_index[w].add(doc_file)
        self._save("investeddata")

    
    def get_key_from_query(self, query):
        words = self._get_word_from_text(query)
        keys = {
            word for word in words
            if word in self.dictionary
        }
        return set(keys)

    

    def _save(self, docs_path):
        invested_index_file = os.path.join(docs_path, "invested_index.pickle")
        dictionary_file= os.path.join(docs_path, "dictionary.txt")

        with open(dictionary_file, mode="w") as f:
            for word in self.invested_index.keys():
                f.write(word + "\n")

        with open(invested_index_file, mode="wb") as f:
            pickle.dump(self.invested_index, f)
    

    def _load(self, docs_path):
        invested_index_file = os.path.join(docs_path, "invested_index.pickle")

        with open(invested_index_file, mode="rb") as f:
            self.invested_index = pickle.load(f)


if __name__ == "__main__":
    docs_path = os.path.join(os.getcwd(), "data")
    index = InvestedIndex()
    index.build_invested_index(docs_path=docs_path, mode="build")