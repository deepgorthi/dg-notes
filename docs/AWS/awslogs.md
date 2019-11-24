# AWSLOGS

AWSLogs can be used in place of Logstash when working with AWS Cloud and ELK stack. 

To install awslogs, we can use:

    pip install awslogs

Groups can be listed using:

    awslogs groups

Streams can be listed using:

    awslogs streams

To capture from a specific stream, we can use:

    awslogs get ${group name} ALL --start="1h"

To capture to a file, we can use:

    awslogs get aws_vpc_log_groups ALL --start='12/05/2019 11:00' --end='12/05/2019 16:00' > vpcflowlog

To remove first 2 columns, use:

    cat vpcflowlog | awk '{print $3 " " $4 " " $5 " " $6 " " $7 " " $8 " " $9 " " $10 " " $11 " " $12 " " $13 " " $14 " " $15 " " $16}' > tmp

Capturing inter VPC communication and to drop intra VPC communication logs, use:

    cat tmp | awk '{ if( $4 ~ /10\.100/ && $5 ~ /10\.100/ ) {} else { print } }' > vpcflowlog


