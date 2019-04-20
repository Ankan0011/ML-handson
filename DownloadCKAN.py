import requests     #API request for uploading the file
import glob         #Creating array of folder location
import os           #For detecting the date from server
import time         #For getting system time comparison
import json         #To convert the response to Json File Format
import wget         #To download the file using a direct link


package_id='mydataset'
url='https://cnrastaging.ogopendata.com/api/3/action/package_show?id='+package_id

dumped_json= '{"help": "https://cnrastaging.ogopendata.com/api/3/action/help_show?name=package_show", "success": true, "result": {"license_title": "License not specified", "maintainer": null, "version": null, "public_access_level": "Public", "relationships_as_object": [], "private": false, "maintainer_email": null, "num_tags": 1, "frequency": "", "contact_name": "yogesh", "id": "c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e", "metadata_created": "2019-01-28T07:55:23.523412", "spatial_coverage": "", "metadata_modified": "2019-02-01T05:34:15.907929", "author": null, "author_email": null, "state": "active", "program": "", "license_id": "notspecified", "type": "dataset", "resources": [{"mimetype": null, "cache_url": null, "hash": "", "description": "test", "data_standard": "", "created": "2019-01-28T07:55:47.703355", "url": "https://cnrastaging.ogopendata.com/dataset/c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e/resource/ba8f4c8c-5dec-4515-827c-ff1294d47e6e/download/test_upload.txt", "datastore_active": false, "format": "TXT", "package_id": "c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e", "cache_last_updated": null, "state": "active", "mimetype_inner": null, "last_modified": "2019-01-28T07:55:47.655087", "position": 0, "revision_id": "b5dea335-ccac-4d28-aae7-485587aac422", "size": 16, "url_type": "upload", "id": "ba8f4c8c-5dec-4515-827c-ff1294d47e6e", "resource_type": null, "name": "test"}, {"mimetype": null, "cache_url": null, "hash": "", "description": "", "data_standard": "", "created": "2019-01-28T07:58:38.966793", "url": "https://cnrastaging.ogopendata.com/dataset/c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e/resource/73553ae5-e950-4603-bb4d-f9df21d20ce5/download/test_upload123.txt", "datastore_active": false, "format": "TXT", "package_id": "c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e", "cache_last_updated": null, "state": "active", "mimetype_inner": null, "last_modified": "2019-01-28T07:58:38.932541", "position": 1, "revision_id": "fb7fc814-dc07-46b0-850d-4a0dfc801b1f", "size": null, "url_type": "upload", "id": "73553ae5-e950-4603-bb4d-f9df21d20ce5", "resource_type": null, "name": "test123"}, {"mimetype": null, "cache_url": null, "hash": "", "description": "", "data_standard": "", "created": "2019-01-28T08:14:21.266706", "url": "https://cnrastaging.ogopendata.com/dataset/c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e/resource/9238f233-5c2d-4335-96fa-6ac3fe30d8fd/download/test_upload2.txt", "datastore_active": false, "format": "TXT", "package_id": "c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e", "cache_last_updated": null, "state": "active", "mimetype_inner": null, "last_modified": "2019-01-28T08:14:21.232466", "position": 2, "revision_id": "90c2b976-a2de-4c03-a4c8-06ffe8359b8a", "size": null, "url_type": "upload", "id": "9238f233-5c2d-4335-96fa-6ac3fe30d8fd", "resource_type": null, "name": "test"}, {"mimetype": null, "cache_url": null, "hash": "", "description": "", "format": "TXT", "url": "https://cnrastaging.ogopendata.com/dataset/c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e/resource/fbd4785d-d547-47db-aed0-a3155caa5132/download/test_upload1.txt", "datastore_active": false, "cache_last_updated": null, "package_id": "c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e", "created": "2019-01-28T10:06:26.875306", "state": "active", "mimetype_inner": null, "last_modified": "2019-01-28T10:06:26.835928", "position": 3, "revision_id": "57539ad4-10c8-4e7a-bcd8-d5a5827eef55", "url_type": "upload", "id": "fbd4785d-d547-47db-aed0-a3155caa5132", "resource_type": null, "size": null}, {"mimetype": null, "cache_url": null, "hash": "", "description": "", "format": "TXT", "url": "https://cnrastaging.ogopendata.com/dataset/c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e/resource/3c09dfd0-2659-4cf9-b7ab-bc45815d0198/download/test_upload1.txt", "datastore_active": false, "cache_last_updated": null, "package_id": "c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e", "created": "2019-01-28T10:16:00.975403", "state": "active", "mimetype_inner": null, "last_modified": "2019-01-28T10:16:00.934916", "position": 4, "revision_id": "ba913382-429b-43ed-b023-a924dde2d739", "url_type": "upload", "id": "3c09dfd0-2659-4cf9-b7ab-bc45815d0198", "resource_type": null, "size": null}, {"mimetype": null, "cache_url": null, "hash": "", "description": "", "name": "Testing1234", "format": "TXT", "url": "https://cnrastaging.ogopendata.com/dataset/c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e/resource/a00d9ae7-067b-4fb0-8c3c-0e3fb897046e/download/test_upload1.txt", "datastore_active": false, "cache_last_updated": null, "package_id": "c3eb30ed-d136-4a40-bf6a-bb3732fd6e6e", "created": "2019-01-28T13:04:12.393203", "state": "active", "mimetype_inner": null, "last_modified": "2019-01-28T13:04:12.335362", "position": 5, "revision_id": "30ca0cdc-1a40-4aa1-9555-6fbc41065410", "url_type": "upload", "id": "a00d9ae7-067b-4fb0-8c3c-0e3fb897046e", "resource_type": null, "size": null}], "limitations": "", "num_resources": 6, "tags": [{"vocabulary_id": null, "state": "active", "display_name": "ocean", "id": "56db6deb-2630-4282-9335-76cece44febd", "name": "ocean"}], "language": "India", "contact_email": "yogeshrpatel2056@gmail.com", "groups": [], "creator_user_id": "6dbd5197-3491-4e7c-9204-061866a23ae5", "relationships_as_subject": [], "publisher": "", "organization": {"description": "This is  a test area for development of OPC services.", "created": "2018-08-13T23:43:09.208542", "title": "Ocean Test", "name": "ocean-test", "is_organization": true, "state": "active", "image_url": "2018-11-30-002349.119330ODPtest.png", "revision_id": "f287aeb2-ae56-4fa7-8a57-057268c7fe24", "type": "organization", "id": "959bdb5d-9554-44fe-b4eb-c3b61651c586", "approval_status": "approved"}, "name": "mydataset", "isopen": false, "url": "", "notes": "test dataset", "owner_org": "959bdb5d-9554-44fe-b4eb-c3b61651c586", "temporal_coverage": "", "title": "mydataset", "revision_id": "a8e0bc58-96d0-463d-8fc1-6200ce5359b9"}}'


headers={"X-CKAN-API-Key": "a52ef25b-a2ed-4966-81ce-23b19985fef6"}
paths = glob.glob("C:\\Users\\ankan.ghosh\\Documents\\*.txt")
output = 'C:\\Users\\ankan.ghosh\\Downloads'
#download_url= ''
#filename = wget.download(download_url)


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

res = requests.post(url)
res_json = json.loads(res.text)
#print(type(res_json))

res2 =item_generator(res_json, 'url')

for x in res2:
    if(x != ''):
        names = wget.download(x , out = output)