#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastQC

By Mingyu Liu
"""

import subprocess
import numpy as np
import os


sample_file = np.loadtxt("./Samples_Name.txt",dtype=str)

sample_name = sample_file[:,1]

# this will download the .sra files to ~/ncbi/public/sra/ (will create directory if not present)
for name in sample_name:
    os.chdir('/hpcstor6/scratch01/m/mingyu.liu001/CUTRUN/' + name)
    fastqc = "/home/mingyu.liu001/Software/FastQC/fastqc -o ./ -f fastq *.fq.gz"
    print ("The command used was: " + fastqc)
    subprocess.call(fastqc, shell=True)
    os.chdir('/hpcstor6/scratch01/m/mingyu.liu001/CUTRUN/')
