#!/usr/bin/python3

import csv, json
import pandas as pd

class Parser_1:
    def __init__(self):
        pass

    def dataset_1(self):
        filename = "data/ransomware_repository.csv"
        dataset = {}
        df = pd.read_csv(filename, skip_blank_lines=True)

        for index, row in df.iterrows():
            d = row.to_dict()
            id = d["ID Number"]
            dataset[id] = d

        return dataset

class Parser_2:
    def __init__(self):
        pass

    def dataset_2(self):
        filename = "data/ransomware.json"
        with open(filename) as json_file:
            dataset = json.load(json_file)
#        print(json.dumps(dataset))

        return dataset
