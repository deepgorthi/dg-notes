# ECS Container Agent

A container agent is ran on an EC2 instance and it helps EC2 instance in joining a cluster. 
The container agent is open-source and can be found [here](https://github.com/aws/amazon-ecs-agent).
The agent runs on ECS optimized or custom AMIs.
On DockerHub - [here](https://hub.docker.com/r/amazon/amazon-ecs-agent/)
There are optional [configuration values](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html). 
Status reports are available when ecs container agent is installed on the EC2 instance. 

Create s3 bucket
```bash
aws> s3api create-bucket --bucket deepu-bucket-ecs-deepdive
```

```
--------------------------------------------
|               CreateBucket               |
+-----------+------------------------------+
|  Location |  /deepu-bucket-ecs-deepdive  |
+-----------+------------------------------+
```

```bash
aws> s3 cp ecs.config s3://deepu-bucket-ecs-deepdive
upload: ./ecs.config to s3://deepu-bucket-ecs-deepdive/ecs.config
```

```bash
aws> s3 ls s3://deepu-bucket-ecs-deepdive
2019-09-03 22:17:09         21 ecs.config
```