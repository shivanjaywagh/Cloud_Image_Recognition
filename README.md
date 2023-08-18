# Cloud_Image_Recognition

S3 Buckets:
Amazon Simple Storage Service is a scalable, high-speed service 
designed for online backup and archiving of data and application programs. Here, S3 is 
used to store the input images sent by the user in an input bucket, and to store the 
results after the image classification of these pre-trained images. 
Autoscaling using CloudWatch: Amazon CloudWatch is a monitoring service for AWS 
resources. In this project, CloudWatch is used to monitor the EC2 instance and SQS 
queue. If the number of messages in the SQS queue exceeds a certain set threshold, 
CloudWatch triggers an alarm that automatically scales up the number of EC2 
instances. Once the number of messages in the queue decreases, CloudWatch scales 
down the number of EC2 instances.
To summarize, the project architecture is designed to handle user requests via the web 
tier, send image processing requests to an SQS queue, process the images using an 
EC2 instance with a pre-trained image classification model, store the preprocessed
images and the processed results in separate S3 buckets, return the output to the user 
using another SQS queue, and automatically scale-up and scale-down on demand 
using CloudWatch. 

Autoscaling:
Firstly, SQS provides a highly available message queuing service that can scale up and 
down automatically on demand. SQS automatically scales the number of servers in 
response to the number of messages in the queue. When there are more messages in 
the queue, SQS will add more servers to handle the increased load. When the number 
of messages decreases, SQS will reduce the number of servers to save resources. This 
automatic scaling ensures that the queue can handle any amount of traffic without 
manual intervention. SQS provides a feature called Auto Scaling, which allows us to 
automatically adjust the number of Amazon EC2 instances based on the number of 
messages in the queue. When the number of messages in the queue exceeds the 
target or range, Autoscaling will launch new instances to handle the load. It will also 
terminate instances if the load is reduced. 
To further support automatic scaling, AWS provides CloudWatch, a monitoring and 
logging service, which allows us to monitor the usage of the application. By setting up 
CloudWatch alarms, we can configure to automatically scale up or down based on the 
usage patterns of the application.
