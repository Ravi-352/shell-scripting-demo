import json
import urllib.parse
import boto3

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Extracting relevant information from the S3 event trigger
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    print(f"File '{object_key}' was uploaded to bucket '{bucket_name}'")

    # Send a notification via SNS

    try:
    	sns_client = boto3.client('sns')
	topic_arn = 'arn:aws:sns:ap-south-1:582443060641:s3-lambda-sns'
	sns_client.publish(
		TopicArn=topic_arn,
		Subject='S3 Object Created',
		Message=f"File '{object_key}' was uploaded to bucket '{bucket_name}'"
	)
    except Exception as e:
        print(e)
	print('Error getting object_key{} from bucket_name{}. Make sure they exist and your bucket is in the same region as this function.'.format(object_key, bucket_name))
	raise e
									              
    return {
        'statusCode': 200,
	        'body': json.dumps('Lambda function executed successfully')
	    }
