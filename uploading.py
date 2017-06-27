import os
import tkinter.filedialog as tkfile

# Here the container to which we have to upload the file to is already pre mentioned.
# This function will upload the file to that container
def uploadAnyFile():
	title = 'Choose File'
	container = 'MyFiles'
	rootDirectory = tk.Tk()
	open = tkfile.askopenfile(parent=rootDirectory,mode='rb',title=title)
	abs_path = os.path.abspath(open.name)
	fileName = os.path.basename(abs_path)
	fileContent=open.read()
	conn.put_object(container,fileName,fileContent,'text/plain')
	
#	In this function you will only be able to upload files if and only if the specified container has enough logically memory capacity!
# 	A file wont be uploaded if the container has enough memory
def restrictedUpload():
	root = tk.Tk()
	open = tkf.askopenfile(parent=root,mode='rb',title='Choose a file')
	max_container_bytes = float(input ('The maximum Kilobytes of a container: '))
	abs_path = os.path.abspath(open.name)
	fName = os.path.basename(abs_path)
	fContent=open.read()
	for container in conn.get_account()[1]:
		print ('Container Size: ', container['bytes'], " bytes.", "in container: ", container['name'])
	container = input ('Enter name of container in which you want to add the file to: ')
	for cont in conn.get_account()[1]:
		print (cont)
		if cont['name'] == container:
			container_bytes = float(float(cont['bytes'])/1024)
			print (container_bytes,max_container_bytes, )
			if max_container_bytes - container_bytes > 0:
				conn.put_object (container, fName, fContent, 'text/plain')
				print ('Element Added')
			else:
				print ('you cant add more elements')
