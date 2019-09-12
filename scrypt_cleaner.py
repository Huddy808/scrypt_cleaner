#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import sys
inFile = sys.argv[1]
shell=True
import subprocess


#use it wnen salt and password together separated by ":"
with open(sys.argv[1], 'rw') as file_handler:
    for line in file_handler:
        linus = line.partition(':')
        linus2 = linus[2].partition('║')
        linus3 = linus2[2].partition('║')
        f=open(sys.argv[1]+".tmp", "a+")
        f.write(linus[0] + '║' +linus3[0] + '║' + linus2[0] + '\n')

import subprocess
out = subprocess.Popen(['rm', sys.argv[1]],
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
wtf = str(sys.argv[1]+".tmp")
wtf2 = wtf.partition('.tmp')
import subprocess
out = subprocess.Popen(['mv', wtf, wtf2[0]],
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)