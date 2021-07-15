#!/bin/bash

set -e

file_name=$1
problem_name=${file_name#*_}

git add $1
git commit -m "Add: solve for ${problem_name%.py} problem."
