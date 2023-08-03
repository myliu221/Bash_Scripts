#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROSE SE

By Mingyu Liu
"""

import subprocess
import numpy as np


sample_file = np.loadtxt("./Samples_Name.txt",dtype=str)

sample_name = sample_file[:,1]

# this will download the .sra files to ~/ncbi/public/sra/ (will create directory if not present)
for name in sample_name:
    mkdir = "mkdir ./" + name
    print ("The command used was: " + mkdir)
    subprocess.call(mkdir, shell=True)
