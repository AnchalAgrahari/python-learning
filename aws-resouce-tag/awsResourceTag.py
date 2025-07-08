import json
import boto3

#reading json file present in s3 bucket
def read_JSON_from_s3(bucket, key):
    try:
        s3_obj = boto3.client('s3')

        s3_clientobj = s3_obj.get_object(Bucket = bucket, Key = key)
        s3_clientdata = s3_clientobj['Body'].read().decode()
        print("Printing s3_clientdata")
        print(s3_clientdata)
        print(type(s3_clientdata))

        s3clientlist = json.loads(s3_clientdata)
        print("json loaded data")
        print(s3clientlist)
        print(type(s3clientlist))

        return s3clientlist
    except Exception as e:
        print("An exception has occured while reading file from s3",e)

#adding tag
def add_tag(bucket_name, data):
    try:
        client = boto3.client('s3')
        tag_set = [{'Key':key, 'Value': value}for key, value in data.items()]
        response = client.put_bucket_tagging(
            Bucket = bucket_name,
            Tagging={
                'TagSet': tag_set
            },
            ExpectedBucketOwner='697429983773'
        )
        print("Tagging Successful")
    except Exception as e:
        print("An exception has occured while tagging", e)

if __name__ == '__main__':
    try:
        
        bucket_name = 'read-json-tagger-file-1062025'
        key = 'tag.json'

        prased_data = read_JSON_from_s3(bucket_name, key)
        print("Let's check data", prased_data)
       
        add_tag(bucket_name, prased_data)
       
    except Exception as e:
        print("An exception has occured", e) 