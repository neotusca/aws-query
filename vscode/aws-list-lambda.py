import sys
import logging
import boto3
from botocore.exceptions import ClientError

def list_resource(region=None):
    # list lambda
    try:
        if region is None:
            rsrc = boto3.client('lambda')
            response = rsrc.list_functions()
            print(response)
        else:
            print("can't retrieve buckets..")
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":
    print ("Hello,world")
    list_resource()
    #list_bucket("ap-northeast-2")
    

