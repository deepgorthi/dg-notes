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

## Resources

Resources represent an object-oriented interface to AWS services. They provide a higher-level abstraction than the raw, low-level calls made by service clients. 

```python
import boto3
s3 = boto3.resource('s3')
sqs = boto3.resource('sqs')
```

## Clients

Clients provide a low-level interface to AWS whose methods map close to one-to-one with service APIs. All service operations are supported by clients. Clients are generated from a JSON service definition file. 

```python
import boto3
sqs = boto3.client('sqs')
```

## Botocore

- Botocore session is encapsulated by Boto3 session. 
- Botocore also maintains credentials and Boto3 can be configured in multiple ways. Regardless of the source that we choose, AWS credentials and region must be set in order to make requests. 
    - ACCESS_KEY: The access key for AWS account
    - SECRET_KEY: The secret key for AWS account
    - SESSION_TOKEN: Used with temporary credentials
- Botocore package provides a low-level interface to AWS services. It is responsible for:
    - Providing access to all available services. 
    - Providing access to all operations within a service. 
    - Marshaling all parameters for a particular operation in the correct format (serialization)
    - Signing the request with the correct authentication signature. 
    - Receiving the response and returning the data in native python data structures (deserialization).
-  Handling higher level abstractions on top of these services is left to the application layer. 
- Botocore package is mainly data-driven. 
- Each service has a JSON description which specifies:  
    - all of the operations the services supports, 
    - all of the parameters the operations accepts, 
    - all of the documentaion related to the service,
    - information about supported regions and endpoints.

## Client vs Resource

|                     Client                     |                    Resource                   |
|:----------------------------------------------:|:---------------------------------------------:|
|  - Exposes Botocore clients to developers      |  - Generated from JSON resource descriptions  |
| - Generated from JSON service descriptions     | - Object-oriented API                         |
| - Provides low-level service access            | - Identifiers and attributes                  |
| - Typically maps one-to-one with service API   | - Actions, References, Sub-resources          |
| - Method names are sname-cases, `list_buckets` | - Collections                                 |

