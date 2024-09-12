import math
import pandas as pd

class GEO_Map():
    __instance = None

    @staticmethod
    def get_instance():
        if GEO_Map.__instance == None:
            GEO_Map()
        return GEO_Map.__instance

    def __init__(self):
        if GEO_Map.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            GEO_Map.__instance = self
            self.map = pd.read_csv("/home/hadoop/python/src/db/uszipsv.csv", 
                                   header=None, names=['A', "B", 'C', 'D', 'E'])
            self.map['A'] = self.map['A'].astype(str)