# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
##############################################################
# 
# Copyright (c) 2018 USTC, Inc. All Rights Reserved
# 
##############################################################
# 
# File:    mean.py
# Author:  roee
# Date:    2018/03/11 16:41:46
# Brief:
# 
# 
##############################################################

import sys

N = 0.0
i = 0

for line in sys.stdin:
    n = float(line.strip().split()[1])
    N += n
    i += 1
    print line

print 'Score\t' + str(N / i)



















# vim: set expandtab ts=4 sw=4 sts=4 tw=100
