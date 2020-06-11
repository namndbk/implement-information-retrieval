import urllib
from urllib.request import urlopen
from urllib.parse import *


class Candidate():
    def __init__(self):
        self.arrayForm = {}
        self.arrayForm["name_vi"] = ""
        self.arrayForm["name_en"] = ""
        self.arrayForm["director"] = ""
        self.arrayForm["actor"] = ""
        self.arrayForm["year"] = ""
        self.arrayForm["kind"] = ""
        self.arrayForm["country"] = ""
        self.arrayForm["flag"] = ""

    def search(self, form):
        query = ""
        self.arrayForm["name_vi"] = form["name_vi"]
        self.arrayForm["name_en"] = form["name_en"]
        self.arrayForm["director"] = form["director"]
        self.arrayForm["actor"] = form["actor"]
        self.arrayForm["year"] = form["year"]
        self.arrayForm["kind"] = form["kind"]
        self.arrayForm["country"] = form["country"]
        self.arrayForm["flag"] = form["flag"]
        if self.arrayForm["flag"] == "1":
            c = " && "
        elif self.arrayForm["flag"] == "2":
            c = " & "
        if self.arrayForm["name_vi"]:
            query += "name_vi:" + '\"' + self.arrayForm["name_vi"] + '\"'
        if self.arrayForm["name_en"]:
            if query != "":
                query += c
            query += "name_en:" + '\"' + self.arrayForm["name_en"] + '\"'
        if self.arrayForm["director"]:
            if query != "":
                query += c
            query += "director:" + '\"' + self.arrayForm["director"] + '\"'
        if self.arrayForm["actor"]:
            if query != "":
                query += c
            query += "actors:" + '\"' + self.arrayForm["actor"] + '\"'
        if self.arrayForm["year"]:
            if query != "":
                query += c
            query += "year:" + '\"' + self.arrayForm["year"] + '\"'
        if self.arrayForm["country"]:
            if query != "":
                query += c
            query += "country:" + '\"' + self.arrayForm["country"] + '\"'
        if self.arrayForm["kind"]:
            if query != "":
                query += c
            query += "kind:" + '\"' + self.arrayForm["kind"] + '\"'
        solr_tuples = [
        	("q", query)
        ]
        print(query)
        print("http://localhost:8983/solr/demo/select?" + urllib.parse.urlencode(solr_tuples))
        conn = urlopen("http://localhost:8983/solr/demo/select?" + urllib.parse.urlencode(solr_tuples))
        rsp = eval(conn.read())
        flag = True
        results = []
        if rsp["response"]["numFound"] != 0:
            count = 0
            for doc in rsp["response"]["docs"]:
                if count < 20:
                    results.append(doc)
                    count += 1
                else:
                    break
        else:
            flag = False
        return results, flag
