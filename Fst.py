# -*- coding: utf-8 -*-

import pynlpir
import sys
import importlib
import jieba

importlib.reload(sys)
# sys.setdefaultencoding("utf-8")

pynlpir.open()
s = '这就是一个恐怖组织，又名基地组织，在2019年实施了卢旺达大屠杀'
segments = pynlpir.segment(s)

for segment in segments:
    print(segment[0],'\t',segment[1])
pynlpir.close()

jb = jieba.cut(s,cut_all=False)
print('jb','/'.join(jb))