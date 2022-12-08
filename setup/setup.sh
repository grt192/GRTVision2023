# update/upgrade all apt packages
sudo apt-get update 
sudo apt-get dist-upgrade

# Install universal tools
sudo apt-get install python3-pip

# setup jetson's ip
./setup_ip.sh

# setup networking
./setup_networking.sh

# setup apriltags
./setup_apriltags.sh