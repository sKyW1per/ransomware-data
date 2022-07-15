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


def main():
    #run your code here

    #parse csv -> dictionary
    blob = get_dataset2()

    #So far, this just prints all data to terminal output.
    print(json.dumps(blob, indent=2))

    print("\ndone!")

if __name__ == "__main__":
    main()
