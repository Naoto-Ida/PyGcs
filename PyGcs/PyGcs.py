# -*- coding: utf-8 -*-

from SearchResult import SearchResult

import urllib2
import json
import re
import sys

class PyGcs:

    api_key = ""
    cx_id = ""
    query = ""
    data = []

    def __init__(self):
        self.set_api_key("")
        self.set_cx_id("")
        self.set_query("")
        pass

    def set_api_key(self, api_key):
        self.api_key = api_key

    def get_api_key(self):
        return self.api_key

    def set_cx_id(self, cx_id):
        self.cx_id = cx_id

    def get_cx_id(self):
        return self.cx_id

    def set_query(self, new_query):
        self.query = new_query

    def get_query(self):
        return self.query

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def search(self, query=None):
        if query is not None:
            self.query = query
        self.query = self.query.replace(' ', '+')

        url = "https://www.googleapis.com/customsearch/v1?key="+self.api_key+"&cx="+self.cx_id+"&q="+self.query+"&alt=json"

        if self.api_key is not "" and self.cx_id is not "" and query is not "":
            try:
                connection = urllib2.urlopen(url)
                res = json.loads(connection.read())
                for r in res["items"]:
                    row = SearchResult(r)
                    self.data.append(row)
                return self.data

            except urllib2.HTTPError, error:
                return None
        else:
            print "something is not set!"

            sys.exit()