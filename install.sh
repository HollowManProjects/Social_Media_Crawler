# This installation script installs
# python3, tweepy and matplotlib. Which are the
# dependencies for this project

sudo apt-get update
sudo apt-get install python3
sudo -H pip install --upgrade pip
sudo pip install tweepy
python3 -m pip install -U matplotlib