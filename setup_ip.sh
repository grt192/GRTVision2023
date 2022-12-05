# Sets static IP of Jetson to 10.1.92.12
# https://elinux.org/Jetson/FRC_Setup#Step_3:_Configuring_Jetpack_Networking

sudo apt-get update 
sudo apt-get install resolvconf

# https://unix.stackexchange.com/a/384699
tee -a /etc/network/interfaces.robot << END
auto eth0
iface eth0 inet static
address 10.1.92.12
netmask 255.0.0.0
gateway 10.1.92.1
network 10.0.0.0
broadcast 10.1.92.255
dns-nameservers 8.8.8.8 8.8.8.4
END

