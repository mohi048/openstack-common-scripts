## Author - Mohit. ((  Git -: http://github.com/mohi048  ))
## Python script to create openstack instance with single network interface
## Tested in Kilo release

###### Define Instance Details ######
instance_name = "test-with-api"
instance_base_image = "25127260-5535-44a6-a9a6-d05d2af0d313"
instance_flavor = "2"
instance_network = "bc2ff223-64ee-4cf6-838a-0508e489313f"

#### Define Openstack Crdentials #####
username = "admin"
password = "admin"
tenant_name = "admin"
auth_url = "http://10.20.30.40:5000/v2.0/"


from novaclient.v2 import client
import time
from datetime import datetime
startTime = datetime.now()
novaConnection = client.Client(username=username, api_key=password, project_id=tenant_name, auth_url=auth_url)
server = novaConnection.servers.create(name = instance_name,image = instance_base_image,flavor = instance_flavor,nics = [{'net-id':instance_network}])
server_status = server.status
ids = server.id
print "Building Instance ID :: ",ids
while server_status == 'BUILD':
	time.sleep(3)
	print "Creating the instance.....with status ",server_status
	print "Time elapsed since ",datetime.now() - startTime
	server = novaConnection.servers.get(server.id)
	server_status = server.status
print "Instance created with status ", server_status
print "Total Time to execute ",datetime.now() - startTime

for network_type,details in novaConnection.servers.find(id=server.id).addresses.iteritems():

	print "##### Network Name ##### ",network_type
	for network in details:
		Network_Details = dict(network)
		for key,values in Network_Details.iteritems():
			print key,"::", values
	print "#######################"
