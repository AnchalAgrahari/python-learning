import json
import boto3

#reading  json file present in systems3clientlist
def read_file_frome_local(file_name):
    try:
        with open(file_name ,'r') as f :
            data = json.load(f)
        print("JSON data read", data)
        return data
    except Exception as e:
        print("AN exception has occured", e)

#adding tag
def add_tag(bucket_name, data_local):
    try:
        client = boto3.client('s3')
        tag_set = [{'Key':key, 'Value':value}for key, value in data_local.item()]
        response = client.put_object_tagging(
            Bucket = bucket_name,
            Tagging={
                'TagSet':tag_set
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

        data_local = read_file_frome_local(file_name)
        print("Let's check data", data_local)

        add_tag(bucket_name, data_local)
       
    except Exception as e:
        print("AN exception has occured", e)