# -*- coding:utf-8 -*-

import re


class Map(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def to_string(self):
        str = 'k = ', self.k, ', v= ', self.v
        return str

    def printValue(self):
        print '(', str(self.k), ',', str(self.v), ')'


def token_stream(str):
    return re.findall(r'\w+', str, re.I)


def mapper(lineNum, list):
    mlist = []
    for item in list:
        mp = Map(''.join([str(lineNum), ':', item]), 1)
        mlist.append(mp)
    return mlist


def combiner(list):
    rdic = {}
    for item in list:
        if rdic.has_key(item.k):
            map = rdic.get(item.k);
            rdic[item.k] = Map(item.k, map.v + 1);
        else:
            map = Map(item.k, 1);
            rdic[item.k] = map
    return rdic.values()


def reducer(dic):
    pass


if __name__ == '__main__':
    file = open('test.log', 'r');

    lineNum = 0;
    while True:
        lineNum += 1;
        line = file.readline()
        if line != '':
            print lineNum, ' ', line, ;
        else:
            break
        list = token_stream(line)
        mlist = mapper(lineNum, list)
        clist = combiner(mlist)
        for item in clist:
            item.printValue()
