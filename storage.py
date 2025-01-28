from google.cloud import storage
from google.cloud import datastore
import os


datastore_client = datastore.Client()
storage_client = storage.Client()


###
# Datastore examples
###
def list_db_entries():
    query = datastore_client.query(kind="photos")

    for photo in query.fetch():
        print(photo.items())

def add_db_entry(object):
    entity = datastore.Entity(key=datastore_client.key('photos'))
    entity.update(object)

    datastore_client.put(entity)


def fetch_db_entry(object):
    query = datastore_client.query(kind='photos')
    for attr in object.keys():
        query.add_filter(attr, "=", object[attr])
    obj = list(query.fetch())
    return obj

###
# Cloud Storage examples
###
def get_list_of_files(bucket_name):
    """Lists all the blobs in the bucket."""
    print("\n")
    print("get_list_of_files: "+bucket_name)

    blobs = storage_client.list_blobs(bucket_name)
    print(blobs)
    files = []
    for blob in blobs:
        files.append(blob.name)

    return files

def upload_file(bucket_name, file_name):
    """Send file to bucket."""
    print("\n")
    print("upload_file: "+bucket_name+"/"+file_name)

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    blob.upload_from_filename(file_name)

    return blob.public_url

def download_file(bucket_name, file_name):
    """ Retrieve an object from a bucket and saves locally"""  
    print("\n")
    print("download_file: "+bucket_name+"/"+file_name)
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)
    blob.download_to_filename(file_name)
    blob.reload()
    return


def uploadImage(image_name,email,time_stamp):
    url = upload_file("cnd_images", "files/"+image_name)
    obj = {"image_name": image_name, "url": url, "email": email, 'timestamp':time_stamp}
    add_db_entry(obj)

def getImages(email):
    obj1 = {'email':email}
    result=fetch_db_entry(obj1)
    image_names = [entry['image_name'] for entry in result] if result else []
    return image_names