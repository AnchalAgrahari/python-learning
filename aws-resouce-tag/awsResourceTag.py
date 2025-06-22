import json
import boto3

#reading  json file present in systems3clientlist
def read_file(file_name):
    try:
        with open(file_name ,'r') as f :
            data = json.load(f)
        print("JSON data read")
        print(data)
        print(type(data))
        return data
    except Exception as e:
        print("AN exception has occured", e)

#reading json file present in s3 bucket
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
    print("An error occured while reading file ",e)

#adding tag
def add_tag(bucket_name, key, data):
    try:
        client = boto3.client('s3')
        response = client.put_object_tagging(
            Bucket = bucket_name,
            Key = key,
            Tagging={
                'TagSet':data
            },
                ExpectedBucketOwner='697429983773'
        )
        print("Tgging Successfull")
    except Exception as e:
        print("An exception has ooccurec while tagging", e)

if __name__ == '__main__':
    try:
        file_name = "tag2.json"
        
        bucket_name = 'read-json-tagger-file-1062025'
        key = 'tag.json'

        data = read_file(file_name)
       
        add_tag(bucket_name, key, data)
       
    except Exception as e:
        print("AN exception has occured", e)