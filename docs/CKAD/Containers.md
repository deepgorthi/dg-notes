# Container

## What is a container

- A container is a self-contained ready-to-run application. 
- Containers have all on board that is required to start the application. 
- To start a container, a container runtime is required. 
- The container runtime is running on a host platform and establishes communication between the localhost kernel and the container. 
- All containers, no matter what they do, run on top of the same local host kernel. 
- On top of container runtime, there are isolated namespaces that help in running different containers. 
- Every virtual machine sits on its own Kernel. On the other hand, Containers run on Container runtime that in turn talks to/ sits on the kernel. 
- Containers are based on features offered by the Linux operating system. 
- `Linux kernel namespaces` provide strict isolation between system components at different levels:
  - network
  - file
  - users
  - processes
  - IPCs
- Linux `cgroups` offer resource allocation and limitation. 

## Container runtimes

- The container runtime allows for starting and running the container on top of the host OS
- The container runtime is responsible for all parts of running the container which are not already a part of the running container program itself
- Different container runtime solutions exist:
  - docker
  - lxc
  - runc
  - cri-o
  - rkt
  - containerd
- These runtimes are included in different container solutions. 

## Understanding OCI

- OCI is the [Open Containers Initiative](https://opencontainers.org) that standardizes the use of containers
  - The `image-spec` defines how to package a container in a `filesystem bundle`
  - The `runtime-spec` defines how to run that filesystem in a container
- OCI standardization ensures compatability between containers, no matter which environment they originally come from. 

## Understanding Container Components

- *Images* are read-only environments that contain the runtime environment which includes the application and all libraries it requires. 
- *Registries* are used to store images. Docker Hub is a common registry, but private registries can be also created. 
- *Containers* are the isolated runtime environments where the application is running. By using `namespaces`, the containers can be offered as a strictly isolated environment. 

## Starting Containers

- On CentOS/RHEL 7, Docker is available from the repositories. 
  - Use `yum install docker` to install
  - Run `docker --version` to verify installation
- One CentOS/RHEL 8, Docker is no longer available
  - use `docker-ce` from Docker.io instead. 
  - After install, use `systemctl enable --now docker` to start and enable the service


