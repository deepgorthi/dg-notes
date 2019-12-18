# [Notes] Learn enough Docker series

## Containers
- Containers are hugely helpful for improving security, reproducibility, and scalability in software development.
- Docker is a platform to develop, deploy, and run applications inside containers.
- A Docker container:
    - `Holds things`
    - `Is portable` — It can be used on your local machine or a cloud provider’s servers.
    - `Has clear interfaces for access` — It has ports that can be opened for interacting through the browser. You can configure it to interact with data through the command line.
    - `Can be obtained from a remote location` — An offsite registry keeps an image for your container.

## Containers vs VMs
The main difference between containers and VMs is in their architectural approach. The one big difference between containers and VMs is that containers *share* the host system’s kernel with other containers.

- VM
    - VMs run on top of a physical machine using a “hypervisor”. A hypervisor, in turn, runs on either a host machine or on “bare-metal”.
    - The host machine provides the VMs with resources, including RAM and CPU. 
    - A guest machine can run on either a hosted hypervisor or a bare-metal hypervisor. 
- Container
    - Containers package up just the user space, and not the kernel or virtual hardware like a VM does. 
    - All the operating system level architecture is being shared across containers. The only parts that are created from scratch are the bins and libs.

## Images
- Images are the immutable master template that is used to pump out containers that are all exactly alike.
- An image contains the Dockerfile, libraries, and code your application needs to run, all bundled together.

## Dockerfile
- A Dockerfile is a file with instructions for how Docker should build your image.

## Docker Platform
- It is Docker’s software that provides the ability to package and run an application in a container on any Linux server. 
- Docker Platform bundles code files and dependencies. 
- It promotes easy scaling by enabling portability and reproducibility.

## Docker Engine
- It is the client-server application.
- Two parts:
    - Community Edition (CE) which is open source.
    - Enterprise Edition (EE which is enterprise oriented and comes with additional features and support.

## Docker Client
- It is the primary way to interact with Docker.
- Docker Client uses the Docker API to send the command from CLI to the Docker Daemon.

## Docker Daemon
- It is the Docker server that listens for Docker API requests. 
- The Docker Daemon manages images, containers, networks, and volumes.

## Docker Volumes 
These are the best way to store persistent data that your apps consume and create. 

## Docker Registry 
It is the remote location where Docker Images are stored. You push images to a registry and pull images from a registry.

## Docker Hub 
It is the largest and default registry of Docker images.

## Docker Repository 
It is a collection of Docker images with the same name and different tags. The tag is the identifier for the image.

## Docker Networking 
It allows you to connect Docker containers together that are either on the same host or multiple hosts.

![Docker flow](img/docker-flow.png)

!!! info "Learn enough Docker"
    - [Part 1](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b)
    - [Part 2](https://towardsdatascience.com/learn-enough-docker-to-be-useful-1c40ea269fa8)
    - [Part 3](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b0b44222eef5)
    - [Part 4](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e)
    - [Part 5](https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421)
    - [Part 6](https://towardsdatascience.com/pump-up-the-volumes-data-in-docker-a21950a8cd8)