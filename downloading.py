# I this we can download the file in the current directory
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