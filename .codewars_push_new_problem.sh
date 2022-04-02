echo "Which folder do you want to push: "
read foldername
echo "Which git message do you want to leave: "
read message
x="/assets/js/main.js"
git add "$foldername"/assets/js/main.js
git commit -m "bash message:  $message "
ssh-add ~/.ssh/id_ed25519
git push
