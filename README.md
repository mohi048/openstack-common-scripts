#create-instance-kilo-openstack.py

This script creates a vm instance on openstack enviroment, Update the following parameters on the script

instance_name = Name of vm to be created, To be put in by user

instance_base_image = Image ID stored in openstack, ID be pulled up by command "glance image-list"

instance_flavor = Instance paramters such as disk/cpu count , ID be pulled up by command "nova flavor-list"

instance_network = Network to be associated by instance , ID to be pulled up by command "neutron net-list"


To execute the script

python create-instance-kilo-openstack.py
