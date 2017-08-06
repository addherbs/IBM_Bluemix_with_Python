import os
import swiftclient


# This function will list the local files in your directory
def showLocal():
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print (f)
			
			
# This function will list all of the containers in your IBM Storage
# List details of the containers
# List Files in the containers with their details as well		
def listFiles():
		#Reads all the containers
		for cont in conn.get_account()[1]:
		print ('Total File Size: ', cont['bytes'], " bytes.", "in cont: ", cont['name'])	#Displays data information of a container
		for dataObj in conn.get_container(cont['name'])[1]:
			print ('object: {0}\t size: {1}\t date: {2}'.format (dataObj['name'], dataObj['bytes'], dataObj['last_modified']))
	
	
# This function will create a new container object in your IBM Storage
def CreateFolder():
		folder=input ('Enter name of folder: ')
		conn.put_container(folder)

# Allow a user to list the contents of any of the remote folders that he wants 
# This will list all the available buckets and you have to name which bucket you want your files to be listed .
def listSomeFiles():
	print ('All the folders are listed here:')
	for folder in conn.get_account()[1]:
		print ("folder Name: ", folder['name'])
	folder = input ('Enter name of folder for which you want to list all the files: ')
	for cont in conn.get_account ()[1]:
		if cont['name'] == folder:
			for data in conn.get_container (cont['name'])[1]:
				print (
					'Data: {0}\t size of data: {1}\t date in bytes: {2}'.format (data['name'], data['bytes'], data['last_modified']))
