#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:52:07 2018

@author: aayushbhargava
"""

import time,os
import commands
import subprocess
print subprocess.call(["cd","ls"])
os.system("cd")
commands.getstatusoutput('cd..')
time.sleep(1)
s=commands.getstatusoutput('ls')
print s[1]

p = subprocess.Popen(["cd","ls"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
# Send input to p.
p.stdin.write("some input\n")
p.stdin.flush()
# Now start grabbing output.
while p.poll() is None:
    l = p.stdout.readline()
    print l
print p.stdout.read()


import subprocess
command='ls'
proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
output= proc.stdout.read()+proc.stderr.read()
print(output)