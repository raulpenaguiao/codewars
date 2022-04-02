#!/bin/bash
ls
echo -n "please input folder name: "
read foldername
echo "your foldername is "
echo $foldername
cp -r ../../template/ ../codewars/
mv template/ $foldername
vim $foldername/assets/js/main.js
echo "now add new files to the git"
