# AWS Certfied Developer Associate (DVA-C01)

## IAM: Identity and Access Management

> Allows you to manage users and also manage their level of access to the AWS Console.

- IAM provides:
    - centralized control over your AWS account.
    - shared access to your AWS account.
    - granular permissions.

- You can enable different levels of access to different users within your organization
- Enables identity federation with Active Directory, Facebook, and LinkedIn, et cetera.
- Allows multifactor authentication.
- Provides temporary access for users or devices and services as necessary, for example, a web or mobile phone application.
- Allows you to set up your own password rotation policy.
- Integrates with many different AWS services.
- **IAM Federation:** Integrate their own repository of users with IAM using SAML standard
- Supports PCI DSS compliance for many applications.

### Users

> End user accessing the services

### Groups 

> Functions (admin, devops) or teams (engineering, design) that contain a group of users.

### Roles 

> Internal usage within AWS resources to define a set of permissions. 

Roles are a secure way to grant permissions to entities you trust that are valid for short durations making them more secure. 
Similar to
    - IAM User in another account.
    - Application code running on an EC2 instance that needs to perform actions on AWS resources
    - An AWS service that needs to act on resources in your account to provide its features.
    - users from a corporate directory who use identity federation with SAML.

### Policies (JSON documents) 

> Defines what each of the Users/Groups/Roles can and cannot do and can be attached to either a user, a group, or a role

They define the permissions for an action regardless of the method that you use to perform the operation.

#### Policy types

- *Identity-based policies*
    - Attach managed and inline policies to IAM identities (users, groups to which users belong, or roles).
    - Identity-based policies grant permissions to an identity.

- *Resource-based policies*
    - Attach inline policies to resources.
    - The most common examples of resource-based policies are Amazon S3 bucket policies and IAM role trust policies.
    - Resource-based policies grant permissions to a principal entity that is specified in the policy. Principals can be in the same account as the resource or in other accounts.

- *Permissions boundaries*
    - Use a managed policy as the permissions boundary for an IAM entity (user or role).
    - That policy defines the maximum permissions that the identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity.

- *Organizations SCPs*
    - Use an AWS Organizations service control policy (SCP) to define the maximum permissions for account members of an organization or organizational unit (OU).
    - SCPs limit permissions that identity-based policies or resource-based policies grant to entities (users or roles) within the account, but do not grant permissions.

- *Access control lists (ACLs)*
    - Use ACLs to control which principals in other accounts can access the resource to which the ACL is attached.
    - ACLs are similar to resource-based policies, although they are the only policy type that does not use the JSON policy document structure.
    - ACLs are cross-account permissions policies that grant permissions to the specified principal entity. ACLs cannot grant permissions to entities within the same account.

- *Session policies*
    - Pass advanced session policies when you use the AWS CLI or AWS API to assume a role or a federated user.
    - Session policies limit the permissions that the role or user's identity-based policies grant to the session. Session policies limit permissions for a created session, but do not grant permissions.

#### IAM Policy Simulator

- When creating new custom policies you can test it here:
    - https://policysim.aws.amazon.com/home/index.jsp
    - This policy tool can you save you time in case your custom policy statement's permission is denied

- Alternatively, you can use the CLI:
    - Some AWS CLI commands (not all) contain `--dry-run` option to simulate API calls. This can be used to test permissions.
    - If the command is successful, you'll get the message: `Request would have succeeded, but DryRun flag is set`
    - Otherwise, you'll be getting the message: `An error occurred (UnauthorizedOperation) when calling the {policy_name} operation`

### IAM Best practices

- One IAM User per person only
- One IAM Role per Application
- IAM credentials should never be shared
- Never write IAM credentials in your code.
- Never use the ROOT account except for initial setup
- It's best to give users the minimal amount of permissions to perform their job.
____

## EC2 Instances

> By default, your EC2 instance comes with:
>
> - A private IP for the internal AWS Network
> - A public IP for the Internet

If your machine is stopped and then restarted, the public IP will change unless Elastic IP is used.

### EC2 User Data

- Bootstrapping means launching commands when a machine starts
- It is possible to bootstrap our instances using an EC2 User data script
- That script is only run once at the instance first start
- Purpose: Ec2 data is used to automate boot tasks such as:
    - Installing updates
    - Installing software
    - Downloading common files from the internet
- The EC2 User Data Script runs with the root user

### EC2 Meta Data

- Information about your EC2 instance
- It allows EC2 isntances to *learn* about themselves without having to use an IAM role for that purpose
- You can retrieve IAM roles from the metadata but not IAM policies
- URL: 169.254.169.254/latest/meta-data

### EC2 Instance Launch Types

- **On Demand Instances**: short workload, predictable pricing
- **Reserved Instances**: long workloads (>= 1 year)
- **Convertible Reserved Instances**: long workloads with flexible instances
- **Scheduled Reserved Instances**: launch within time window you reserve
- **Spot Instances**: short workloads, for cheap, can lose instances
- **Dedicated Instances**: no other customers will share your hardware
- **Dedicated Hosts**: book an entire physical server, control instance placement

#### On-Demand Instance

- Pay for what you use
- Has the highest cost but no upfront payment
- No long term commitment
- Linux instances are by the second whereas Windows instances are currently by the hour.
- Good for applications with short-term or spiky or unpredictable workloads that cannot be interrupted

#### Reserved Instances

- Up to 75% off compared to On-demand
- Pay upfront for what you use with long term commitment
- Reservation period can be 1 or 3 years
- Reserve a specific instance type
- Recommended for steady state usage applications like database systems

#### Convertible Reserved Instances

- Can change the EC2 instance type
- Up to 54% discount compared to On-Demand

#### Scheduled Reserved Instances

- Launch within time window you reserve
- When you require a fraction of a day / week / month

#### Spot Instances

- Can get a discount of up to 90% compared to On-demand
- You bid a price and get the instance as long as its under the price
- Price varies based on offer and demand
- Spot instances are reclaimed within a 2 minute notification warning when the spot price goes above your bid
- Used for batch jobs, Big Data analysis, or workloads that are resilient to failures
- Not great for critical jobs or databases

#### Dedicated Instances

- Instances running on hardware that’s dedicated to you
- May share hardware with other instances in same account
- No control over instance placement (can move hardware after stop / start)

#### Dedicated Hosts

- Physical dedicated EC2 server for your use
- Full control of Ec2 Instance placement
- Visibility into the underlying sockets / physical cores of the hardware
- Allocated for your account for a 3 year period reservation
- Expensive
- Useful for software that have a complicated licensing model (Bring your own License)
- Or for a companies that have strong regulatory or compliance needs

#### Which host is right for me

- On demand: coming and staying in resort whenever we like, we pay the full price
- Reserved: like planning ahead and if we plan to stay for a long time, we may get a good discount.
- Spot instances: the hotel allows people to bid for the empty rooms and the highest bidder keeps the rooms.You can get kicked out at any time
- Dedicated Hosts: We book an entire building of the resort

### EC2 Pricing

- EC2 instances prices (per hour) varies based on these parameters:
    - Region you are in
    - Instance Type you’re using
    - On-Demand vs Spot vs Reserved vs Dedicated Host
    - Linux vs Windows vs Private OS (RHEL, Windows)
    - You are billed by the second, with a minimum of 60 seconds.
    - You also pay for other factors such as storage, data transfer, fixed IP public addresses, load balancing
    - You do not pay for the instance if the instance is stopped

### AMI

- AWS comes with base images such as:
    - Ubuntu
    - Fedora
    - RedHat
    - Windows
- These images can be customized at runtime using EC2 User data
- AMI – an image that can be customized by the user and used to create instances
- AMIs can be built for Linux or Windows machines
- *AMI are built for a specific AWS region*

- Using a custom built AMI can provide the following advantages:
    - Pre-installed packages needed
    - Faster boot time (no need for long ec2 user data at boot time
    - Machine comes configured with monitoring / enterprise software
    - Security concerns – control over the machines in the network
    - Control of maintenance and updates of AMIs over time
    - Active Directory Integration out of the box
    - Installing your app ahead of time (for faster deploys when auto-scaling)
    - Using someone else’s AMI that is optimized for running an app, DB, etc.

### EC2 Instances Overview

- Instances have 5 distinct characteristics advertised on the website:
    - The RAM (type, amount, generation)
    - The CPU (type, make, frequency, generation, number of cores)
    - The I/O (disk performance, EBS optimisations)
    - The Network (network bandwidth, network latency
    - The Graphical Processing Unit (GPU)

- It may be daunting to choose the right [instance type](https://aws.amazon.com/ec2/instance-types/)
- https://ec2instances.info/ can help with summarizing the types of instances
- R/C/P/G/H/X/I/F/Z/CR are specialised in RAM, CPU, I/O, Network, GPU

#### Dr. McGift Phx

- F1 - field programmable gate array
    - use case for this is genomic research, financial analytics, real time video processing big data
- I3 - high speed storage
    - NosQL databases, data warehousing
- G3 - Graphic intensive
    - Video encoding, 3D application streaming
- H1 - High Disk Throughput
    - Mapreduce workloads, distributed filesystems such as HDFS, MapR-FS
- T2 - Lowest cost general purpose computing
    - Webservers, small database servers
- D2 - Dense storage
    - File servers, data warehousing, Hadoop
- R4 - Memory optimized
- M5 - General purposed and balanced
    - For application servers
- C5 - Compute optimized
    - CPU intensive apps and database servers
- P3 - Graphics or general purpose GPU
    - Machine learning, bitcoin mining
- X1 - Memory optimized
    - SAP HANA, Apache Spark
- M instance types are *balanced* (Main purpose)
- *T2/T3 instance types are “burstable”*

#### Burstable Instances (T2)

- AWS has the concept of burstable instances (T2 machines)
- Burst means that overall, the instance has OK CPU performance.
- When the machine needs to process something unexpected (a spike in load for example), it can burst, and CPU can be VERY good.
- If the machine bursts, it utilizes “burst credits”
- If all the credits are gone, the CPU becomes BAD
- If the machine stops bursting, credits are accumulated over time
- Burstable instances can be amazing to handle unexpected traffic and getting the insurance that it will be handled correctly
- If your instance consistently runs low on credit, you need to move to a different kind of non-burstable instance.

#### T2 Unlimited

- Nov 2017: It is possible to have an unlimited burst credit balance
- You pay extra money if you go over your credit balance, but you don’t lose in performance
- Overall, it is a new offering, so be careful, costs could go high if you’re not monitoring the health of your instances
_____

## EBS Volume

- An EC2 machine loses its root device volume (main drive) when it is manually terminated.
- Unexpected terminations might happen from time to time and you need a way to store your instance data somewhere

> An EBS (Elastic Block Store) Volume is a network drive you can attach to your instances while they run. It allows your instances to persist data. Once attached, you create a file system on top of these volumes, and you can run a database or you can install applications or you can store files on there, etc.

- It’s a network drive (Not a physical drive)
    - It uses the network to communicate the instance, which means there might be a bit of latency
    - It can be detached from an EC2 instance and attached to another one quickly
- It is locked to an Availability Zone (AZ)
    - An EBS Volume in us-east-1a cannot be attached to us-east-1b
    - An EBS volume doesn't exist on just one physical disk. It is actually spread across an availability zone.
    - *To move a volume across, you first need to snapshot it*
- Have a provisioned capacity (size in GB and IOPS)
    - You get billed for all the provisioned capacity
    - You can increase the capacity of the drive over time

### EBS Volume Types

- EBS Volumes come in 4 types and are characterized in Size | Throughput | IOPS
  - **General Purpose - GP2 (SSD):** General purpose SSD volume that balances price and performance for a wide variety of workloads.
    - You get a ratio of 3 IOPS per GB with up to 10,000 IOPS
    - Ability to burst up to 3,000 IOPS for extended periods of time for volumes at 3,334 GB and above.
  - **Provisioned IOPS - IO1 (SSD):** Highest-performance SSD volume for mission-critical low-latency or high-throughput workloads
    - For things like intensive applications, relational databases, NoSQL databases.
    - Use this when you need more than 10,000 IOPS. Can provision up to 20,000 IOPS per volume.
  - **Throughput Optimized - ST1 (HDD):** Low cost HDD volume designed for frequently accessed, throughput-intensive workloads
    - Used for BigData, data warehousing, log processing, etc.
    - Cannot be boot volume.
  - **Cold Hard disk Drive - SC1 (HDD):** Lowest cost HDD volume designed for less frequently accessed workloads
    - Used for File server.
    - Cannot be boot volume.

### EBS Volume Resizing

- *Feb 2017: You can resize your EBS Volumes*
- After resizing an EBS volume, you need to repartition your drive

### EBS Snapshots

- EBS Volumes can be backed up using Snapshots.
- Snapshots only take the actual space of the blocks on the volume
- If you snapshot a 100 GB drive that only has 5 GB of data, then your EBS snapshot will only be 5 GB
- Snapshots are used for:
    - *Backups*: ensuring you can save your data in case of catastrophe
    - *Volume migration*
        - Resizing a volume down
        - Changing the volume type
        - Encrypting a volume

### EBS Encryption

- When you create an encrypted EBS volume, you get the following:
    - Data at rest is encrypted inside the volume
    - All the data in flight moving between the instance and the volume is encrypted
    - All snapshots are encrypted
    - All volumes created from the snapshots are encrypted
- Encryption and decryption are handled transparently
- Encryption has a minimal impact on latency
- EBS Encryption leverages keys from KMS (AES-256)
- Copying an unencrypted snapshot allows encryption

### EBS vs. Instance Store

- Some instance do not come with Root EBS volumes
- Instead, they come with Instance Store
- Instance store is physically attached to the machine
- Pros:
    - Better I/O performance
- Cons:
    - On termination, the instance store is lost
    - You can’t resize the instance store
    - Backups must be operated by the user
- Overall, EBS-backed instances should fit most application workloads

### EBS Summary

- EBS can be attached to only one instance at a time
- EBS volumes are locked at the AZ level
- Migrating an EBS volume across AZ means first backing it up (snapshot), then recreating it in the other AZ
- EBS backups use IO and you shouldn’t run them while your application is handling a lot of traffic
- Root EBS Volumes of instances get terminated by default if the EC2 instance gets terminated. (You can disable that)

_____
