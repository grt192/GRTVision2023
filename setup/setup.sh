# cwd to this script's directory
cd "$(dirname "$0")"

# update/upgrade all apt packages
sudo apt-get -y update 
sudo apt-get -y dist-upgrade

# Install universal tools
sudo apt-get -y install python3-pip

# setup jetson's ip
./setup_ip.sh

# setup networking
./setup_networking.sh

# setup apriltags
./setup_apriltags.sh