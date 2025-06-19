import json
import boto3

#reading  json file present in system
def read_file(file_name):
    try:
        with open(file_name ,'r') as f :
            data = json.load(f)
        print(data)
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

def add_tag(bucket_name):
    try:
        client = boto3.client('s3')
        response = client.put_bucket_tagging(
            Bucket = bucket_name , 
            ChecksumAlgorithm = 'CRC32',
            Tagging={
                'TagSet':  s3clientlist[ 's3clientlist']
            },
            ExpectedBucketOwner='697429983773'
        )
    except Exception as e:
        print("An exception has occured during tagging",e)

def lambda_handler(event, context):
    try:
         # s3
        bucket_name = 'read-json-tagger-file-1062025'
        #add tag
        add_tag(bucket_name)
    except Exception as e:
        print("An exception has occured")


if __name__ == '__main__':
    try:
        file_name = "tag.json"
        #file reading
        read_file(file_name)
        ##
        event = {}
        context = None
        lambda_handler(event, context)
       
    except Exception as e:
        print("AN exception has occured", e)