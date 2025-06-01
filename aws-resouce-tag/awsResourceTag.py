import json
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

    
