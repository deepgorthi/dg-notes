# Lambda Programming Model

## Handler 

[^1] Handler is the function AWS Lambda calls to start execution of your Lambda function. You identify the handler when you create your Lambda function. When a Lambda function is invoked, AWS Lambda starts executing your code by calling the handler function. 

## Context

AWS Lambda also passes a context object to the handler function, as the second parameter. Via this context object your code can interact with AWS Lambda. 

## Logging 

- Your Lambda function can contain logging statements. AWS Lambda writes these logs to CloudWatch Logs. 
- Log data can be lost due to throttling or, in some cases, when the execution context is terminated.

## Exceptions

Your Lambda function needs to communicate the result of the function execution to AWS Lambda.

## Concurrency

When your function is invoked more quickly than a single instance of your function can process events, Lambda scales by running additional instances.

## Bootstrapping

- Your Lambda function code must be written in a stateless style, and have no affinity with the underlying compute infrastructure. [^2] 
- Bootstrapping refers to the process of preparing the environment before an application starts to resolve and process an incoming request. 
- Bootstrapping is done in two places: 
    - in the entry script 
    - in the application


[^1]: [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/programming-model-v2.html)
[^2]: [Runtime bootstrapping](https://www.yiiframework.com/doc/guide/2.0/en/runtime-bootstrapping)