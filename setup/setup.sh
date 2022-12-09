# cwd to this script's directory
cd "$(dirname "$0")"
# allow all scripts in this directory to be executed
sudo chmod -R u+x ./

# update/upgrade all apt packages
sudo apt-get update 
sudo apt-get upgrade

# Install universal tools
sudo apt-get -y install python3-pip

# setup jetson's ip
echo "------------------------"
echo "IP SETUP -------------------------------------------------- IP SETUP"
./setup_ip.sh

# setup networking
echo "------------------------"
echo "NETWORKING SETUP ---------------------------------------------- NETWORKING SETUP"
./setup_networking.sh

# setup apriltags
echo "------------------------"
echo "APRILTAG SETUP ---------------------------------------------- APRILTAG SETUP"
./setup_apriltags.sh

# setup streaming
echo "------------------------"
echo "STREAMING SETUP ---------------------------------------------- STREAMING SETUP"
./setup_streaming.sh