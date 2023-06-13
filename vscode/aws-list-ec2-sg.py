import sys
import logging
import pprint
import boto3
from botocore.exceptions import ClientError

def list_resource(region=None):
    # list ec2
    try:
        if region is None:
            ec2 = boto3.client('ec2')
            response = ec2.describe_security_groups()
            #print(response)
            parse(response, 1)
            
        else:
            print("can't retrieve buckets..")
    except ClientError as e:
        logging.error(e)
        return False
    return True

def parse(dicta, level):
    #print(dicta, type(dicta))
    try:
        sg = dicta['SecurityGroups']
        cnt = 1
        #print(sg, type(sg),"+++++")
        
        for key in sg:
            #print(key, type(key),"=====")            
            print(cnt,"/",key['GroupId'],"/",key['GroupName'],"/",key['Description'])
                        
            if len(key['IpPermissions']) == 0:    ## not assign "inbound" info.
                print("  -/ inbound")

            for sgrule in key['IpPermissions']:   ## for inbound
                print("   / inbound")
                #print("in /", sgrule, type(sgrule))
                if 'FromPort' in sgrule:
                    print("      //", sgrule['IpProtocol'],"/", sgrule['FromPort'],"/",sgrule['ToPort'])
                else:
                    if sgrule['IpProtocol'] == '-1':
                        print("      // All / Any / Any")
                    else:
                        print("      //", sgrule['IpProtocol'],"/ null / null")

                #print(sgrule['IpRanges'], type(sgrule['IpRanges']))
                for iprange in sgrule['IpRanges']:
                    #print("-ir------/",iprange, type(iprange))
                    if 'Description' in iprange:
                        print("         ///", iprange['CidrIp'],"/", iprange['Description'])
                    else:
                        print("         ///", iprange['CidrIp'],"/ null")
                for grouppair in sgrule['UserIdGroupPairs']:
                    #print("-gp------/",grouppair, type(grouppair))
                    if 'Description' in grouppair:
                        print("         ///", grouppair['GroupId'],"/", grouppair['Description'])
                    else:
                        print("         ///", grouppair['GroupId'],"/ null")
            

            if len(key['IpPermissionsEgress']) == 0:
                print("  -/ outbound")

            for sgrule in key['IpPermissionsEgress']:  ## for outbound
                print("   / outbound")
                #print("out/", sgrule, type(sgrule))
                if 'FromPort' in sgrule:
                    print("      //", sgrule['IpProtocol'],"/", sgrule['FromPort'],"/",sgrule['ToPort'])
                else:
                    if sgrule['IpProtocol'] == '-1':
                        print("      // All / Any / Any")
                    else:
                        print("      //", sgrule['IpProtocol'],"/ null / null")

                #print(sgrule['IpRanges'], type(sgrule['IpRanges']))
                for iprange in sgrule['IpRanges']:
                    #print("-ir------/",iprange, type(iprange))
                    if 'Description' in iprange:
                        print("         ///", iprange['CidrIp'],"/", iprange['Description'])
                    else:
                        print("         ///", iprange['CidrIp'],"/ null")
                for grouppair in sgrule['UserIdGroupPairs']:
                    #print("-gp------/",grouppair, type(grouppair))
                    if 'Description' in grouppair:
                        print("         ///", grouppair['GroupId'],"/", grouppair['Description'])
                    else:
                        print("         ///", grouppair['GroupId'],"/ null")




            print('--------------------------------------')
            print()
            cnt = cnt + 1
            

    except:
        print('ERROR')
        return False
    return True



if __name__ == "__main__":
    print ("***** AWS security group *****")
    list_resource()
    #list_bucket("ap-northeast-2")
    

