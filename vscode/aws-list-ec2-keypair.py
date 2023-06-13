import sys
import logging
import boto3
from botocore.exceptions import ClientError

def list_resource(region=None):
    # list ec2-keypair
    try:
        if region is None:
            ec2 = boto3.client('ec2')
            response = ec2.describe_key_pairs()
            #print(response, type(response))
            parse(response, 1)
        else:
            print("can't retrieve resources..")
    except ClientError as e:
        logging.error(e)
        return False
    return True

def parse(dictionary, level):
    #print(level)
    try:
        #print(list(dictionary))
        #print(dictionary['KeyPairs'], type(dictionary['KeyPairs']))
        #print("========================")
        for aa in dictionary['KeyPairs']:
            #print(aa, type(aa))
            #print(aa['KeyPairId'], aa['KeyName'])
            print("KeyPairID : %s, KeyName : %s" % (aa['KeyPairId'], aa['KeyName']) )
        

        #print(dictionary.items())
    except:
        return False
    return True



if __name__ == "__main__":
    list_resource()
    #list_bucket("ap-northeast-2")
    

