# S3-Hello-World
Amazon Web Service S3 Hello World

Simple code to use with trial Amazon S3

Create keys
- In IAM Console click users on the left
- Then Create New Users at the top
- put in a username
- download keys
- put keys in ~/.aws/credentials
```
[default]
aws_access_key_id = YOURKEY
aws_secret_access_key = YOURSECRETKEY
```
- In IAM create a group, called Administrators
- Select the user, the action is add to group
- Create a bucket in S3 management console

Using Python and boto3
- pip install boto3
- Documentation at: https://boto3.readthedocs.org/en/latest/reference/services/index.html

