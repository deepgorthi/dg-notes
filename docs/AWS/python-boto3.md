# Python Boto3

Boto3 is the AWS SDK for Python. It provides easy to use object-oriented API and low-level access to AWS services. 

Botocore provices the low-level clients, session, credentials and configuration data. Boto3 is built on top of Botocore by providing its own sessions, resources and collections. 

## Session

A session manages state about a particular configuration. By default, a session is created for you when needed. However, it is possible and recommended to maintain your own sessions in some scenarios. Sessions typically store:

- Credentials
- Region
- Other configurations

## Configuration

In addition to credentials, you can also configure non-credential values. In general, boto3 follows the same approach used in credential lookup: try various locations until a value is found. Boto3 uses these sources for configuration:

- Explicitly passed as the config parameter when creating a client. 
- Environment variables
- ~/.aws/config


