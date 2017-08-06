import swiftclient
import os

# Get the Environment Variables from the IBM Bluemix cloudfoundry
# Environment Variables
auth_url= "auth_url"
project_id= "project_id"
region= "dallas"
user_id= "user_id"
username= "username",
password= "password"


# Makes sure Connection object is global
#Initializes the connection
#Call this everytime if the conn is not global
def get_connection():
    conn = swiftclient.Connection(
        key=password,
        authurl=auth_url+"/v3",
        auth_version='3',
        os_options={
            "project_id": project_id,
            "user_id": user_id,
            "region_name": region})
