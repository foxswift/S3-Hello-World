#!/usr/bin/env python
# list buckets, and Objects

import boto3

def main():
   s3=boto3.resource('s3')
   for bucket in s3.buckets.all():
      print('Bucket = ' + bucket.name)
      for key in bucket.objects.all():
         print('\tObject Key = ' + key.key)



if __name__ == '__main__':
   main()
