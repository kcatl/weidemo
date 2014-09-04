#!/usr/bin/python2

path = '/root/weibo/conf/testfile.txt'
file = open(path, 'r')
token = file.read().split()
a, b = token
print len(token), a, b