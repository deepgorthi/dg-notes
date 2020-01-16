# Terraform Basics

## Features

- **Infrastructure as Code**
    - Idempotent: Even if the scripts are run multiple times, nothing will be changed if the configuration is already in place. 
    - High-Level Syntax (Hashicorp Configuration Language)
    - Easiily re-usable (with the help of modules) 

- **Executioon Plans**
    - Shows the inent of the deploy: What is going to be deployed, changed or deleted. 
    - Helps ensure everything in the development is intentional. 

- **Resource Graph**
    - Illustrates all changes and dependencies


## Use Cases

- **Hybrid Clouds**
    - Cloud agnostic
    - Allows deployments to multiple providers simultaneously

- **Multi-tier architecture**
    - Allows deployment of several layers of architecture
    - Usually able to automatically deploy in the correct order

- **Software-defined Networking**
    - Able to deploy network architecture

- **Used for**
    - High-level Infrastructure orchestration tool
    - Not for configuration management
    - Need to be used in conjuctioon with configuration managment tools like Ansible. 
    - Provides *provisioners* that can call tools like Ansible to perform the configuration management process. 


## Installation

```bash

# Install Docker CE
    # Install Utils:
        $ sudo yum install -y yum-utils \
        device-mapper-persistent-data \
        lvm2
    # Add the Docker repository:
        $ sudo yum-config-manager \
            --add-repo \
            https://download.docker.com/linux/centos/docker-ce.repo
    # Install Docker CE:
        $ sudo yum -y install docker-ce

# Start Docker and enable it:
    $ sudo systemctl start docker && sudo systemctl enable docker

# Add cloud_user to the docker group:
    $ sudo usermod -aG docker <user_name>

# Test the Docker installation:
    $ docker --version

# Configuring Swarm Manager node
    # On the manager node, initialize the manager:
        $ docker swarm init \
        --advertise-addr [PRIVATE_IP]

# Configure the Swarm Worker node
    # On the worker node, add the worker to the cluster:
        $ docker swarm join --token [TOKEN] \
            [PRIVATE_IP]:2377

# Verify the Swarm cluster
    # List Swarm nodes:
        $ docker node ls

# Install Terraform
    # Install Terraform 0.11.13 on the Swarm manager:
        $ sudo curl -O https://releases.hashicorp.com/terraform/0.12.18/terraform_0.12.18_linux_amd64.zip
        $ sudo yum install -y unzip
        $ sudo unzip terraform_0.12.18_linux_amd64.zip -d /usr/local/bin/

# Test the Terraform installation:
    $ terraform version
```