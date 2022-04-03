#!/bin/bash
cd javascript
ls
cd ..
echo -n "please input folder name: "
read foldername
echo "your foldername is "
echo $foldername
cp -r ../../template/ ../codewars/
mv template/ javascript/$foldername
vim javascript/$foldername/assets/js/main.js
echo "now add new files to the git"
