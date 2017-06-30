# How to delete a file from a container
def deleteFile():
    containerName=input ('Enter name of container: ')
    fileName=input ('Enter file name to delete: ')
    try:
        conn.delete_object(containerName,fileName)
    except:
        print ('File Does not Exist.')