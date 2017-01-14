#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import itertools
import operator
import numpy as np
import nltk
import sys
import sys
import os
import time
#import py_compile
#py_compile.compile('hputool.py')
import hputool
import imp
imp.reload(hputool)
from datetime import datetime
import polyglot
from polyglot.downloader import downloader
from polyglot.text import Text, Word
from polyglot.text import Text
from rnn import RNN

#text = Text(u"Đó là con đường biển ngắn nhất để đi từ Ấn_Độ_Dương sang Thái_Bình_Dương")
#print(text.entities)
print("Starting...")
hputool.convert_coll_dataset("./data/train.trans", "./data/train.parser")
print("Finished")
#scores = [3.0, 1.0, 0.2]
#print HPUTOOL.softmax(scores)
'''blob = """The Israeli Prime Minister Benjamin Netanyahu has warned that Iran poses a "threat to the entire world"."""
text = Text(blob)
text.entities'''