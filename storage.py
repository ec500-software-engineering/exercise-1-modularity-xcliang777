# Copyright 2018 Gang Wei wg0502@bu.edu
# storage module


class storage():
    def __init__(self,bo,bp,pul):
        self.bo = bo
        self.bp = bp
        self.pul = pul
    def filter(self):
        return 0
    #for useful data
    # connection to the database
    # storage the data into the database
    # extract the data out of the database of the format
    def read(self,Input):
        if Input == "bo":
            return self.bo
        elif Input == "bp":
            return self.bp
        elif Input == "pul":
            return self.pul