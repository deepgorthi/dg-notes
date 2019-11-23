# ECS Task Definitions

[Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) describe how Docker images should be ran. 

Each Task Definition can control 1 or more containers (with optional volumes)

Applications can be 1 or more task definitions. 

Grouped containers run on the same instance. This can be used for minimum latency. 

Services are created through task definitions.

Components of Task definition.
- Family -> Used for versioning the Task Definition when it is modified.
- [Container definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)
- Volumes -> A way to share data between containers. 

```bash
aws> ecs register-task-definition --cli-input-json file://web-task-definition.json
```

```
------------------------------------------------------------------------------------------------
|                                    RegisterTaskDefinition                                    |
+----------------------------------------------------------------------------------------------+
||                                       taskDefinition                                       ||
|+--------+-----------+---------+-------------------------------------------------------------+|
|| family | revision  | status  |                      taskDefinitionArn                      ||
|+--------+-----------+---------+-------------------------------------------------------------+|
||  web   |  1        |  ACTIVE |  arn:aws:ecs:us-east-1:289503391411:task-definition/web:1   ||
|+--------+-----------+---------+-------------------------------------------------------------+|
|||                                      compatibilities                                     |||
||+------------------------------------------------------------------------------------------+||
|||  EC2                                                                                     |||
||+------------------------------------------------------------------------------------------+||
|||                                   containerDefinitions                                   |||
||+-----------+------------------------+----------------+------------------+-----------------+||
|||    cpu    |       essential        |     image      |     memory       |      name       |||
||+-----------+------------------------+----------------+------------------+-----------------+||
|||  102      |  True                  |  nginx         |  50              |  nginx          |||
||+-----------+------------------------+----------------+------------------+-----------------+||
||||                                      portMappings                                      ||||
|||+-----------------------------------+-------------------------+--------------------------+|||
||||           containerPort           |        hostPort         |        protocol          ||||
|||+-----------------------------------+-------------------------+--------------------------+|||
||||  80                               |  80                     |  tcp                     ||||
|||+-----------------------------------+-------------------------+--------------------------+|||
```

```bash
aws> ecs list-task-definition-families
----------------------------
|ListTaskDefinitionFamilies|
+--------------------------+
||        families        ||
|+------------------------+|
||  web                   ||
|+------------------------+|
```

```bash
aws> ecs list-task-definitions
----------------------------------------------------------------
|                      ListTaskDefinitions                     |
+--------------------------------------------------------------+
||                     taskDefinitionArns                     ||
|+------------------------------------------------------------+|
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:1  ||
|+------------------------------------------------------------+|
```

```bash
aws> ecs describe-task-definition --task-definition web:1
------------------------------------------------------------------------------------------------
|                                    DescribeTaskDefinition                                    |
+----------------------------------------------------------------------------------------------+
||                                       taskDefinition                                       ||
|+--------+-----------+---------+-------------------------------------------------------------+|
|| family | revision  | status  |                      taskDefinitionArn                      ||
|+--------+-----------+---------+-------------------------------------------------------------+|
||  web   |  1        |  ACTIVE |  arn:aws:ecs:us-east-1:289503391411:task-definition/web:1   ||
|+--------+-----------+---------+-------------------------------------------------------------+|
|||                                      compatibilities                                     |||
||+------------------------------------------------------------------------------------------+||
|||  EC2                                                                                     |||
||+------------------------------------------------------------------------------------------+||
|||                                   containerDefinitions                                   |||
||+-----------+------------------------+----------------+------------------+-----------------+||
|||    cpu    |       essential        |     image      |     memory       |      name       |||
||+-----------+------------------------+----------------+------------------+-----------------+||
|||  102      |  True                  |  nginx         |  50              |  nginx          |||
||+-----------+------------------------+----------------+------------------+-----------------+||
||||                                      portMappings                                      ||||
|||+-----------------------------------+-------------------------+--------------------------+|||
||||           containerPort           |        hostPort         |        protocol          ||||
|||+-----------------------------------+-------------------------+--------------------------+|||
||||  80                               |  80                     |  tcp                     ||||
|||+-----------------------------------+-------------------------+--------------------------+|||
```

After registering task definition under family web for 4 times
```bash
aws> ecs list-task-definitions
----------------------------------------------------------------
|                      ListTaskDefinitions                     |
+--------------------------------------------------------------+
||                     taskDefinitionArns                     ||
|+------------------------------------------------------------+|
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:1  ||
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:2  ||
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:3  ||
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:4  ||
|+------------------------------------------------------------+|
```

You can deregister any task definition
```bash
aws> ecs deregister-task-definition --task-definition web:3
```

```
aws> ecs list-task-definitions
----------------------------------------------------------------
|                      ListTaskDefinitions                     |
+--------------------------------------------------------------+
||                     taskDefinitionArns                     ||
|+------------------------------------------------------------+|
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:1  ||
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:2  ||
||  arn:aws:ecs:us-east-1:289503391411:task-definition/web:4  ||
|+------------------------------------------------------------+|
```

To create a task definition template
```bash
aws> ecs register-task-definition --generate-cli-skeleton
```


```bash
aws> ecs run-task --cluster deepdive --task-definition web --count 1
--------------------------------------------------------------------------------------------------------------------------
|                                                         RunTask                                                        |
+------------------------------------------------------------------------------------------------------------------------+
||                                                         tasks                                                        ||
|+----------------------+-----------------------------------------------------------------------------------------------+|
||  clusterArn          |  arn:aws:ecs:us-east-1:289503391411:cluster/deepdive                                          ||
||  containerInstanceArn|  arn:aws:ecs:us-east-1:289503391411:container-instance/6368caa4-6386-4a5b-9c60-ac752591b819   ||
||  cpu                 |  102                                                                                          ||
||  createdAt           |  1567610699.64                                                                                ||
||  desiredStatus       |  RUNNING                                                                                      ||
||  group               |  family:web                                                                                   ||
||  lastStatus          |  PENDING                                                                                      ||
||  launchType          |  EC2                                                                                          ||
||  memory              |  50                                                                                           ||
||  taskArn             |  arn:aws:ecs:us-east-1:289503391411:task/798b90f2-ffaf-4bd0-a2dd-10842dfd1d9f                 ||
||  taskDefinitionArn   |  arn:aws:ecs:us-east-1:289503391411:task-definition/web:5                                     ||
||  version             |  1                                                                                            ||
|+----------------------+-----------------------------------------------------------------------------------------------+|
|||                                                     containers                                                     |||
||+-----------------+--------------------------------------------------------------------------------------------------+||
|||  containerArn   |  arn:aws:ecs:us-east-1:289503391411:container/4ccb5949-e4c6-47d7-92a8-066b9d7c4cf4               |||
|||  cpu            |  102                                                                                             |||
|||  lastStatus     |  PENDING                                                                                         |||
|||  memory         |  50                                                                                              |||
|||  name           |  nginx                                                                                           |||
|||  taskArn        |  arn:aws:ecs:us-east-1:289503391411:task/798b90f2-ffaf-4bd0-a2dd-10842dfd1d9f                    |||
||+-----------------+--------------------------------------------------------------------------------------------------+||
|||                                                      overrides                                                     |||
||+--------------------------------------------------------------------------------------------------------------------+||
||||                                                containerOverrides                                                ||||
|||+-----------------------------------------------------+------------------------------------------------------------+|||
||||  name                                               |  nginx                                                     ||||
|||+-----------------------------------------------------+------------------------------------------------------------+|||
```