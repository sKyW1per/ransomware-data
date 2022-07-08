#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

#Import all code from the parsers.py file
from parsers import *


def get_dataset1():
    #parse dataset_1
    P = Parser_1()
    mydata = P.dataset_1()

    return mydata

def count_values(blob):
    years = {}
    for i in blob:
        try:
            y = blob[i]["Year"]
            y_int = int(y)
            if y_int not in years:
                years[y_int] = 0
            years[y_int] += 1
        except ValueError:
            pass
    return years

def main():
    #run your code here

    #parse csv -> dictionary
    blob = get_dataset1()
    years = count_values(blob)


    #make graph with matplotlib
    titles = list(years.keys())
    values = list(years.values())
    plt.plot(titles, values)
    plt.ylabel('Aantal aanvallen per jaar')

    #for testing: show the graph
    #plt.show()

    #print the graph to a png and store the png in the "output" folder
    plt.savefig('output/graph_1.png')


    print("\ndone!")
    print("het resultaat staat nu in de 'output' folder.")
    print("Documentnaam: graph1.png")


if __name__ == "__main__":
    main()
