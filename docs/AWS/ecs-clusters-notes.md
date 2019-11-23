# ECS Clusters

To create a cluster
```bash
aws> ecs create-cluster --cluster-name deepdive
```

Here is the output
```
------------------------------------------------------------------------------------------------
|                                         CreateCluster                                        |
+----------------------------------------------------------------------------------------------+
||                                           cluster                                          ||
|+------------------------------------+-------------------------------------------------------+|
||  activeServicesCount               |  0                                                    ||
||  clusterArn                        |  arn:aws:ecs:us-east-1:289503391411:cluster/deepdive  ||
||  clusterName                       |  deepdive                                             ||
||  pendingTasksCount                 |  0                                                    ||
||  registeredContainerInstancesCount |  0                                                    ||
||  runningTasksCount                 |  0                                                    ||
||  status                            |  ACTIVE                                               ||
|+------------------------------------+-------------------------------------------------------+|
|||                                         settings                                         |||
||+--------------------------+---------------------------------------------------------------+||
|||  name                    |  containerInsights                                            |||
|||  value                   |  disabled                                                     |||
||+--------------------------+---------------------------------------------------------------+||
```

To list clusters
```bash
aws> ecs list-clusters
```

Here is the output
```
-----------------------------------------------------------
|                      ListClusters                       |
+---------------------------------------------------------+
||                      clusterArns                      ||
|+-------------------------------------------------------+|
||  arn:aws:ecs:us-east-1:289503391411:cluster/deepdive  ||
|+-------------------------------------------------------+|
```

To describe a specific cluster
```bash
aws> ecs describe-clusters --clusters deepdive
```

Here is the output
```
------------------------------------------------------------------------------------------------
|                                       DescribeClusters                                       |
+----------------------------------------------------------------------------------------------+
||                                          clusters                                          ||
|+------------------------------------+-------------------------------------------------------+|
||  activeServicesCount               |  0                                                    ||
||  clusterArn                        |  arn:aws:ecs:us-east-1:289503391411:cluster/deepdive  ||
||  clusterName                       |  deepdive                                             ||
||  pendingTasksCount                 |  0                                                    ||
||  registeredContainerInstancesCount |  0                                                    ||
||  runningTasksCount                 |  0                                                    ||
||  status                            |  ACTIVE                                               ||
|+------------------------------------+-------------------------------------------------------+|
|||                                         settings                                         |||
||+--------------------------+---------------------------------------------------------------+||
|||  name                    |  containerInsights                                            |||
|||  value                   |  disabled                                                     |||
||+--------------------------+---------------------------------------------------------------+||
```

To delete a cluster
```bash
aws> ecs delete-cluster --cluster deepdive
```
