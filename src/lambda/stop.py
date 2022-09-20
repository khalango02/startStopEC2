import boto3
import traceback

def stopInstances(event, lambda_context):
    print('Stopping instances ...')
    ec2_client = boto3.client('ec2')
    region = 'us-east-1'

    ec2_client = boto3.client('ec2', region_name=region)
    instances = ec2_client.describe_instances()
    instanceIds = list()
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == "running" and not instance['Tags'] is None : 
                for tag in instance['Tags']:
                    try:
                        if tag['Key'] == 'environment' and tag['Value'] == 'lab1Cles'    :
                            instanceIds.append(instance['InstanceId'])
                    except:
                        print ("Not expected error: ", traceback.print_exc())
              
    if len(instanceIds) > 0 : 
        print ("Stopping instances: " + str(instanceIds))
        ec2_client.stop_instances(InstanceIds=instanceIds, Force=False)                                                   