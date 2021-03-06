# -*- coding:utf-8 -*-

import re


def token_stream(line):
    return re.findall(r'\w+', line, re.I)


def mapper(lineNum, list):
    dic = {}
    for item in list:
        key = ''.join([str(lineNum), ':', item])
        if (dic.has_key(key)):
            ll = dic.get(key)
            ll.append(1)
            dic[key] = ll
        else:
            dic[key] = [1]

    return dic


def reducer(dic):
    keys = dic.keys()
    rdic = {}
    for key in keys:
        lineNum, kk = key.split(":")
        ss = ''.join([lineNum, ':', str(dic.get(key))])
        if (rdic.has_key(kk)):
            ll = rdic[kk]
            ll.append(ss)
            rdic[kk] = ll
        else:
            rdic[kk] = [ss]

    return rdic


def combiner(dic):
    keys = dic.keys();
    tdic = {}
    for key in keys:
        valuelist = dic.get(key)
        count = 0;
        for i in valuelist:
            count += i;
        tdic[key] = count;
    return tdic


def shuffle(dic):
    dict = sorted(dic.iteritems(), key=lambda x: x[0])
    return dict


def get_reverse_index(filepath):
    file = open(filepath, 'r');
    lineNum = 0;
    rdic_p = {}
    while True:
        lineNum += 1;
        line = file.readline()
        if line != '':
            # print lineNum, ' ', line, ;
            pass
        else:
            break
        list = token_stream(line)
        mdic = mapper(lineNum, list)
        cdic = combiner(mdic)
        # print cdic
        rdic_p.update(cdic)

    rdic = reducer(rdic_p)

    # sdic = shuffle(rdic)
    return rdic


if __name__ == '__main__':
    # if __name__ == '__main1__':

    filepath = 'test.log'

    filepath = raw_input("please input filepath of file ：");
    dic = get_reverse_index(filepath)

    search_word = raw_input("please input the word you want to search ：");

    if (dic.has_key(search_word)):
        print dic.get(search_word)
    else:
        print -1

# if __name__ == '__main__':
if __name__ == '__main2__':
    dic = {'a': 31, 'bc': 5, 'c': 3, 'asd': 4, 'aa': 74, 'd': 0}
    dict = sorted(dic.iteritems(), key=lambda x: x[1])
    print dict
