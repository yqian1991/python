#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Yu Qian

def word_count(file_path):
    file = open(file_path, 'r+')
    num = 0
    file.read()
    for line in file:
        print line
        line_list = line.split()
        num += len(line_list)
    file.close()
    return num

if __name__ == '__main__':
    try:
        print 'The total number of words is :', word_count("/Users/Yu/OMtest/omsignal-bver/lib/ombver/build/omsdk.rb")
    except Exception, e:
        print "Can't open file!"