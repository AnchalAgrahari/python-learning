import json
import boto3
try:

    s3_obj = boto3.client('s3')

    s3_clientobj = s3_obj.get_object(Bucket = 'read-json-tagger-file-1062025', Key = 'tag.json')
    s3_clientdata = s3_clientobj['Body'].read().decode()

    print("Printing s3_clientdata")
    print(s3_clientdata)
    print(type(s3_clientdata))

    s3clientlist = json.loads(s3_clientdata)
    print("json loaded data")
    print(s3clientlist)
    print(type(s3clientlist))
except Exception as e:
    print("An error occured", e)

def read_file(file_name):
    try:
        with open(file_name ,'r') as f :
            data = json.load(f)
        print(data)
    except Exception as e:
        print("AN exception has occured", e)

    

if __name__ == '__main__':
    try:
        file_name = 'tag.json'
        read_file(file_name)

    except Exception as e:
        print("AN exception has occured", e)

    
