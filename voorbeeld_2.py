#!/usr/bin/python3

import matplotlib.pyplot as plt
import json

#Import all code from the parsers.py file
from parsers import *


def get_dataset2():
    #parse dataset_2
    P = Parser_2()
    mydata = P.dataset_2()

    return mydata

def count_values(blob):
    years = {}
    for v in blob["values"]:
        if "meta" in v:
            for m in v["meta"]:
                if "date" in m:
                    date_unchanged = v["meta"]["date"]
                    date_splitted = str.split(date_unchanged)
                    t = date_splitted[1].isnumeric()
                    y = [e for e in date_splitted if e.isnumeric()]
                    y_int = int(y[0])
                    if y_int not in years:
                        years[y_int] = 0
                    years[y_int] += 1
    return years

def main():
    #run your code here

    #parse csv -> dictionary
    blob = get_dataset2()
    years = count_values(blob)
    years_sorted = sorted(years)
    print(years)
    # make graph with matplotlib

    titles = list(years_sorted)
    values = []
    for y in sorted(years):
        print(y)
        values.append(years[y])

    plt.plot(titles, values)
    plt.ylabel('Aantal waarnemingen per jaar')

    # for testing: show the graph
#    plt.show()

    # print the graph to a png and store the png in the "output" folder
    plt.savefig('output/graph_2.png')

    print("\ndone!")

if __name__ == "__main__":
    main()
