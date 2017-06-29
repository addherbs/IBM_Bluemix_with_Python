# Use the dependencies from connection.py and listing.py
# Using this function we can download the file in the current directory
def downloadFile():
    listFiles()
    containerName=input ('Enter name of container: ')
    fileName=input ('Enter file name to download: ')
    try:
        filesContent=conn.get_object(containerName,fileName)
        str=filesContent[1]
        print('File Download successful. First Line of file is:')
        print(stri.splitlines()[0])
    except:
        print('File Does not Exist.')
		
		
def listFiles():
		for cont in conn.get_account()[1]:
		print ('Total File Size: ', cont['bytes'], " bytes.", "in cont: ", cont['name'])
		for dataObj in conn.get_container(cont['name'])[1]:
			print ('object: {0}\t size: {1}\t date: {2}'.format (dataObj['name'], dataObj['bytes'], dataObj['last_modified']))