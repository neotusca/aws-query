import logging
import boto3
from botocore.exceptions import ClientError

def list_bucket(region=None):
    # list bucket
    try:
        if region is None:
            s3 = boto3.client('s3')
            response = s3.list_buckets()
            
            for bucket in response['Buckets']:
                print(f'  {bucket["Name"]}')
        else:
            print("can't retrieve buckets..")
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":
    print ("Hello,world")
    list_bucket()
    #list_bucket("ap-northeast-2")
    

