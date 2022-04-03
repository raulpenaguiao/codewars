#!/bin/bash
cd python
ls
cd ..
echo -n "please input folder name: "
read foldername
echo "your foldername is "
echo $foldername
mkdir python/$foldername
vim python/$foldername/$foldername.py
echo "now add new files to the git"
