import boto3
import os

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', '')
ACCESS_SECRET = os.getenv('AWS_ACCESS_SECRET', '')
REGION = os.getenv('AWS_REGION', 'eu-west-3')
INSTANCE_ID = os.getenv('AWS_MC_INSTANCE_ID', '')
SERVER_IP = os.getenv('AWS_MC_SERVER_IP', '')

def startServer() -> str:
    if ACCESS_KEY == '' or ACCESS_SECRET == '' or REGION == '':
        print('Please provice a valid key/secret')
        return ''
    if INSTANCE_ID == '':
        print('Please provice a valid instance id')
        return ''

    try:
        ec2 = boto3.resource('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=ACCESS_SECRET, region_name=REGION)

        # Check if the instance is stopped
        response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
        state = response['Reservations'][0]['Instances'][0]['State']['Name']

        if state == 'stopped':
            # Start the instance
            ec2.start_instances(InstanceIds=[INSTANCE_ID])
            return f'Server is starting at {SERVER_IP}. Map on: http://{SERVER_IP}:8123'
        else:
            return f'Server is already running at {SERVER_IP}. Map on: http://{SERVER_IP}:8123'
    except:
        return ''
