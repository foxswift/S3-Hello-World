#!/usr/bin/env python
# upload a test file

import boto3

def main():
   s3=boto3.resource('s3')
   
   data = open('/tmp/TestFile.jpg', 'rb')
   s3.Bucket('dmf-hello-world').put_object(Key='TestFile.jpg', Body=data)


if __name__ == '__main__':
   main()
