import requests     #API request for uploading the file
import glob         #Creating array of folder location
import os           #For detecting the date from server
import time         #For getting system time comparison


url='https://cnrastaging.ogopendata.com/api/action/resource_create'
data={"package_id":"mydataset","name": "Testing1234"}
headers={"X-CKAN-API-Key": "a52ef25b-a2ed-4966-81ce-23b19985fef6"}
paths = glob.glob("C:\\Users\\ankan.ghosh\\Documents\\*.txt")

for x in paths :
    file=x
    files=[('upload', open(file))] 
    if(((time.time() - os.path.getmtime(file)) / 3600) < 1):
        res = requests.post(url, data=data, headers=headers, files=files) 
        print(res.text)
    else:
        print("Nothing to Upload")