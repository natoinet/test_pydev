'''
Created on 10/12/2014

@author: antoinebrunel
'''
from csv import reader

if __name__ == '__main__':
    filename = "kw-test.csv"

    import sys
    print(sys.getdefaultencoding())

    #with open(filename) as f:
    #with open(filename, mode='rt') as f:
    with open(filename, mode='rt', encoding='utf-8') as f:
        csvreader = reader(f)
        for keyword in csvreader:
                kw = keyword[0]
                print(kw)
