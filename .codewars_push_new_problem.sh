echo "Which git message do you want to leave: "
read $message
git commit -m "$message"
ssh-add ~/.ssh/id_ed25519
git push
