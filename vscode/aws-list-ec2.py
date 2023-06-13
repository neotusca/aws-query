import sys
import logging
import boto3
from botocore.exceptions import ClientError

def list_resource(region=None):
    # list ec2
    try:
        if region is None:
            ec2 = boto3.client('ec2')
            response = ec2.describe_instances()
            print(response, type(response))
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
    

