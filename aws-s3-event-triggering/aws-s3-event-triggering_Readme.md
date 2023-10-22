OBJECTIVE: \n
Automate the Notification service (SNS) to Subscribers upon updating new content in Cloud (AWS S3 storage bucket)

PREREQUISITES: "\n"
Up-to-date linux terminal with aws-cli configured: For documentation refer - "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html"\n
Install 'jq' and 'zip' packages in the terminal. \n
Stable Internet connection. \n


REQUIREMENTS THAT THE SCRIPT TAKES CARE OF:
AWS S3 bucket \n
AWS SNS topic \n
AWS Lambda function which gets invoked by s3 service whenever there is an upload in s3 bucket and inturn invokes SNS topic to publish message to subscribers \n


Steps:
1. Clone/Fork the Repository
Command: git clone https://github.com/Ravi-352/shell-scripting-demo.git
2. In Linux Terminal, go to "aws-s3-event-triggering" folder
  a. S3-lambda-function.py (lambda function definition/code) inside the directory s3-lambda-function
  b. s3-notification-triggering.sh
  c. sample_file.txt to test "sns publish"

Steps involed in "s3-notification-triggering"
  a. Creating an iam role with AWSLambda and AWSSNS full access
  ![image](https://github.com/Ravi-352/shell-scripting-demo/assets/91112573/f4bbb90b-4e99-4e3a-836d-af77b039d00a)

  b. Creating an S3 bucket
  ![image](https://github.com/Ravi-352/shell-scripting-demo/assets/91112573/18be5967-c43e-4f75-b70e-74a6815e2719)

  c. Creating a lambda function and giving s3 service permissions to invoke this lambda function
  ![image](https://github.com/Ravi-352/shell-scripting-demo/assets/91112573/a0592c18-22e1-4d34-982e-e8cff15da16e)

  ![image](https://github.com/Ravi-352/shell-scripting-demo/assets/91112573/c891cf75-5f43-4d8a-8c65-ac618eb886d0)

  d. Creating SNS topic and making it send notofocation to request for user subscription with user email as endpoint - 
  ![image](https://github.com/Ravi-352/shell-scripting-demo/assets/91112573/8fde798f-9a78-42dc-9994-22735cf37034)

  ![image](https://github.com/Ravi-352/shell-scripting-demo/assets/91112573/31d7c1aa-5894-48b8-b7b4-305461b9cf16)

Tada! Once user accepts the subscription request from email, User will get updates on any new update event happening in the service provider's AWS s3 bucket, 
User will get email-notification.






