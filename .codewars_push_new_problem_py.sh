echo "Which folder do you want to push: "
read foldername
echo "Which git message do you want to leave: "
read message
git add python/$foldername/$foldername.py
git commit -m "bash message:  $message "
ssh-add ~/.ssh/id_ed25519
git push
