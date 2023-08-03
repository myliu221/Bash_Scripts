#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROSE SE

By Mingyu Liu
"""

import subprocess
import numpy as np
import os


sample_file = np.loadtxt("./Samples_Name.txt",dtype=str)

sample_name = sample_file[:,1]

# this will download the .sra files to ~/ncbi/public/sra/ (will create directory if not present)
for name in sample_name:
    os.chdir('/hpcstor6/scratch01/m/mingyu.liu001/LNCas9/' + name)
    cat_R1 = "cat /hpcstor6/scratch01/m/mingyu.liu001/LNCas9/" + name + "*_R1_*.fastq.gz > " + name + "_R1.fastq.gz"
    cat_R2 = "cat /hpcstor6/scratch01/m/mingyu.liu001/LNCas9/" + name + "*_R2_*.fastq.gz > " + name + "_R2.fastq.gz"
    print ("The command used was: " + cat_R1)
    print ("The command used was: " + cat_R2)
    subprocess.call(cat_R1, shell=True)
    subprocess.call(cat_R2, shell=True)
    os.chdir('/hpcstor6/scratch01/m/mingyu.liu001/LNCas9/')
