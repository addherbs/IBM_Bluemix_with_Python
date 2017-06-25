
# This function will list the local files in your directory
dwdef showLocal():
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print (f)
			
			
# This function will list all of the containers in your IBM Storage
# List details of the containers
# List Files in the containers with their details as well		
def listFiles():
		for cont in conn.get_account()[1]:
		print ('Total File Size: ', cont['bytes'], " bytes.", "in cont: ", cont['name'])
		for dataObj in conn.get_container(cont['name'])[1]:
			print ('object: {0}\t size: {1}\t date: {2}'.format (dataObj['name'], dataObj['bytes'], dataObj['last_modified']))
	
	
# This function will create a new container object in your IBM Storage
def CreateFolder():
		folder=input ('Enter name of folder: ')
		conn.put_container(folder)
