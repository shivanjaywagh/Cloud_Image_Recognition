import boto3
import subprocess

# Create SQS client
sqs = boto3.client('sqs',region_name='',aws_access_key_id='',
                          aws_secret_access_key='')
s3 = boto3.client('s3',region_name='',aws_access_key_id='',
                          aws_secret_access_key='')

queue_url = ''

queue_url_output = ''

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=3,
    MessageAttributeNames=[
        'All'
    ],
    WaitTimeSeconds=0
)

#print(response)
if 'Messages' in response:
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    filename = message['Body']
    #print(filename)
    #print('Received message: %s' % filename)

    s3.download_file('cloudydays-project1-s3bucket-input', filename, "downloaded_images/"+filename)
    inpara = "downloaded_images/"+filename
    classification = subprocess.run(['python3','image_classification.py',inpara],capture_output=True)

    classification_str = classification.stdout.decode('utf-8')

    # Send message to SQS queue
    sqs.send_message(
    QueueUrl=queue_url_output,
    MessageBody=classification_str)

    message_body = filename+","+classification_str

    new_filename = filename.replace(".JPEG",".txt")

    #Upload object to s3
    s3.put_object(Bucket="", Body=message_body, Key=new_filename)

    print("All Done!")
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
)
else:
    print("No Messages found in queue")
