#!/bin/bash

# Sample slurm submission script for the Chimera compute cluster
# Lines beginning with # are comments, and will be ignored by
# the interpreter.  Lines beginning with #SBATCH are directives
# to the scheduler.  These in turn can be commented out by
# adding a second # (e.g. ##SBATCH lines will not be processed
# by the scheduler).
#
#
# set name of job
#SBATCH --job-name=MY_ANALYSIS
#
# set the number of processors/tasks needed
#SBATCH -n 10

#set an account to use
#if not used then default will be used
# for scavenger users, use this format:
##SBATCH --account=pi_first.last
# for contributing users, use this format:
##SBATCH --account=<deptname|lastname>

# set max wallclock time  DD-HH:MM:SS
#SBATCH --time=00-10:00:00

# set a memory request
#SBATCH --mem=100gb

# Set filenames for stdout and stderr.  %j can be used for the jobid.
# see "filename patterns" section of the sbatch man page for
# additional options
#SBATCH --error=%x-%j.err
#SBATCH --output=%x-%j.out
#

# set the partition where the job will run.  Multiple partitions can
# be specified as a comma separated list
# Use command "sinfo" to get the list of partitions
#SBATCH --partition=Intel6126


# Put your job commands here, including loading any needed
# modules or diagnostic echos.

module load bowtie2-2.4.2-gcc-10.2.0-4o66eku 

bowtie2-build /hpcstor6/scratch01/m/mingyu.liu001/Ecoli_reference/genome.fa Ecoli



# this job simply reports the hostname and sleeps for two minutes

echo "using $SLURM_CPUS_ON_NODE CPUs"
echo `date`

hostname
sleep 120

# Diagnostic/Logging Information
echo "Finish Run"
echo "end time is `date`"