import urllib
from urllib.request import urlopen
from urllib.parse import *
from util import classify  
from singleton import Singleton


@Singleton
class Candidate():
    def __init__(self):
        self.arrayForm = {}
        self.arrayForm["name"] = ""
        self.arrayForm["director"] = ""
        self.arrayForm["actor"] = ""
        self.arrayForm["year"] = ""
        self.arrayForm["kind"] = ""
        self.arrayForm["country"] = ""
        self.arrayForm["flag"] = ""

    def search(self, form):
        query = ""
        self.arrayForm["name"] = form["name"]
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
        category = classify(self.arrayForm["name"], 2)
        if category:
            query += "name_vi:" + '\"' + self.arrayForm["name"] + '\"'
        else:
            query += "name_en:" + '\"' + self.arrayForm["name"] + '\"'
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
        print("http://localhost:8983/solr/release/select?" + urllib.parse.urlencode(solr_tuples))
        conn = urlopen("http://localhost:8983/solr/release/select?" + urllib.parse.urlencode(solr_tuples))
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
