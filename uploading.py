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