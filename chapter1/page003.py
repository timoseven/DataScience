#!/usr/bin/python
#-*- coding: utf-8 -*-

sentence = "Petr Piper picked a peck of pickled pepper A peck of pickled \
        peppers Peter Piper picked If Peter Piper picked a peck of pickled \
        peppers Wheres the peck of pickled peppers Peter Piper picked"

####初始化一个字典对象
word_dict = {}

#词频统计
for word in sentence.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] +=1
#这样会输出每次的，这个是字典，可以跳出for循环打印对应的
        print (word, word_dict[word])

