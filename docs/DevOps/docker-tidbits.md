# Docker Tidbits

??? info "Source: Learn enough Docker"
    - [Part 1](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b)
    - [Part 2](https://towardsdatascience.com/learn-enough-docker-to-be-useful-1c40ea269fa8)
    - ** [Part 3](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b0b44222eef5)
    - ** [Part 4](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e)
    - [Part 5](https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421)
    - [Part 6](https://towardsdatascience.com/pump-up-the-volumes-data-in-docker-a21950a8cd8)


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

A Docker container needs a host to run on. This can either be a physical machine or a VM, either on-prem or in the cloud. The host has the Docker daemon and client running which enables you to interact with a Docker registry on the one hand (to pull/push Docker images), and on the other hand, allows you to start, stop and inspect containers.

![Docker flow](img/docker-flow.png)

For single host deployments, data can be exchanged via `shared volumes`. This introduces tight coupling and it will be harded to translate a single host deployment into a multihost deployment. The upside, though, is speed for shared volumes. 

In multihost deployments, we need to consider how are containers communicating within the host and how does communication paths look between different hosts. We need to take care of both performance and security aspects. 

Docker networking is the native container SDN solution:

- **Bridge Mode (default)**: Docker daemon creates docker0, a virtual Ethernet bridge that automatically forwards packets between any other network interfaces that are attached to it. Connects all containers on a host to this internal network through creating a pair of peer interfaces.
- **Host Mode**: Using host mode networking, the container effectively inherits the IP address from its host. This mode is faster than the bridge mode as there is no routing overhead, but it exposes the container directly to the public network and its security implications.
- **Container mode**: Docker will re-use the networking namespace of another container. The second container that started with `--net=container:<first_container_name>` has the same IP address as the first container. Kubernetes networking uses this mode. 
- **No Networking**: This mode puts the container inside of its own network stack but doesn’t configure it.
    - For containers that don’t need a network like batch jobs writing to a disk volume
    - For containers that will be configured with custom networking.

**Note**: By default, Docker has inter-container communication enabled [`--icc=true`]. Containers on a host can communicate without any restrictions which may lead to Denial of Service attacks. 


## Docker Compose 
It is a tool to run apps that require multiple Docker containers and allows us to move commands into a docker-compose.yml file for reuse.


## Docker Services
> Services are really just “containers in production.” A service only runs one image, but it codifies the way that image runs — what ports it should use, how many replicas of the container should run so the service has the capacity it needs, and so on. Scaling a service changes the number of container instances running that piece of software, assigning more computing resources to the service in the process.


## Dockerfile
A container is built from a series of layers. Each layer is read only, except the final container layer that sits on top of the others. The Dockerfile tells Docker which layers to add and in which order to add them.

When an image is pulled from a remote repository to a local machine only layers that are not already on the local machine are downloaded.

Layers are created in the final image only with these commands. 

- FROM
- RUN
- COPY
- ADD

All other commands (`Dockerfile INSTRUCTIONS`) configure, or do other tasks that does effect the image directly. 

Here are the Dockerfile INSTRUCTIONS:

- `FROM` — specifies the base (parent) image.
- `LABEL` — provides metadata. Good place to include maintainer info.
- `ENV` — sets a persistent environment variable.
- `RUN` — runs a command and creates an image layer. Used to install packages into containers.
- `COPY` (recommended) — copies files and directories to the container. 
- `ADD` — copies files and directories to the container. Can upack local .tar files. (ADD does the same thing as COPY, but has two more use cases. ADD can be used to move files from a remote URL to a container and ADD can extract local TAR files.) ADD instruction contains the \ line continuation character.
- `CMD` — provides a command and arguments for an executing container. Parameters can be overridden. There can be only one CMD.
- `WORKDIR` — sets the working directory for the instructions that follow.
- `ARG` — defines a variable to pass to Docker at build-time.
- `ENTRYPOINT` — provides command and arguments for an executing container. Arguments persist.
- `EXPOSE` — exposes a port. EXPOSE does not actually publish the port. It acts as a information relay betweenthe one building the image and the one who is running the container. Use docker run with the `-p` flag to publish and map one or more ports at run time. The uppercase `-P` flag will publish all exposed ports.
- `VOLUME` — creates a directory mount point to access and store persistent data.

??? info "Cheatsheet"
    [Source cheatsheet](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)

    `FROM`

    Usage:

    FROM <image>
    FROM <image>:<tag>
    FROM <image>@<digest>
    Information:
    FROM must be the first non-comment instruction in the Dockerfile.
    FROM can appear multiple times within a single Dockerfile in order to create multiple images. Simply make a note of the last image ID output by the commit before each new FROM command.
    The tag or digest values are optional. If you omit either of them, the builder assumes a latest by default. The builder returns an error if it cannot match the tag value.
    Reference - Best Practices

    `MAINTAINER`

    Usage:

    MAINTAINER <name>
    The MAINTAINER instruction allows you to set the Author field of the generated images.

    Reference

    `RUN`

    Usage:

    RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux or cmd /S /C on Windows)
    RUN ["<executable>", "<param1>", "<param2>"] (exec form)
    Information:

    The exec form makes it possible to avoid shell string munging, and to RUN commands using a base image that does not contain the specified shell executable.
    The default shell for the shell form can be changed using the SHELL command.
    Normal shell processing does not occur when using the exec form. For example, RUN ["echo", "$HOME"] will not do variable substitution on $HOME.
    Reference - Best Practices

    `CMD`

    Usage:

    CMD ["<executable>","<param1>","<param2>"] (exec form, this is the preferred form)
    CMD ["<param1>","<param2>"] (as default parameters to ENTRYPOINT)
    CMD <command> <param1> <param2> (shell form)
    Information:

    The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well.
    There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect.
    If CMD is used to provide default arguments for the ENTRYPOINT instruction, both the CMD and ENTRYPOINT instructions should be specified with the JSON array format.
    If the user specifies arguments to docker run then they will override the default specified in CMD.
    Normal shell processing does not occur when using the exec form. For example, CMD ["echo", "$HOME"] will not do variable substitution on $HOME.
    Reference - Best Practices

    `LABEL`

    Usage:

    LABEL <key>=<value> [<key>=<value> ...]
    Information:

    The LABEL instruction adds metadata to an image.
    To include spaces within a LABEL value, use quotes and backslashes as you would in command-line parsing.
    Labels are additive including LABELs in FROM images.
    If Docker encounters a label/key that already exists, the new value overrides any previous labels with identical keys.
    To view an image’s labels, use the docker inspect command. They will be under the "Labels" JSON attribute.
    Reference - Best Practices

    `EXPOSE`

    Usage:

    EXPOSE <port> [<port> ...]
    Information:

    Informs Docker that the container listens on the specified network port(s) at runtime.
    EXPOSE does not make the ports of the container accessible to the host.
    Reference - Best Practices

    `ENV`

    Usage:

    ENV <key> <value>
    ENV <key>=<value> [<key>=<value> ...]
    Information:

    The ENV instruction sets the environment variable <key> to the value <value>.
    The value will be in the environment of all “descendant” Dockerfile commands and can be replaced inline as well.
    The environment variables set using ENV will persist when a container is run from the resulting image.
    The first form will set a single variable to a value with the entire string after the first space being treated as the <value> - including characters such as spaces and quotes.
    Reference - Best Practices

    `ADD`

    Usage:

    ADD <src> [<src> ...] <dest>
    ADD ["<src>", ... "<dest>"] (this form is required for paths containing whitespace)
    Information:

    Copies new files, directories, or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.
    <src> may contain wildcards and matching will be done using Go’s filepath.Match rules.
    If <src> is a file or directory, then they must be relative to the source directory that is being built (the context of the build).
    <dest> is an absolute path, or a path relative to WORKDIR.
    If <dest> doesn’t exist, it is created along with all missing directories in its path.
    Reference - Best Practices

    `COPY`

    Usage:

    COPY <src> [<src> ...] <dest>
    COPY ["<src>", ... "<dest>"] (this form is required for paths containing whitespace)
    Information:

    Copies new files or directories from <src> and adds them to the filesystem of the image at the path <dest>.
    <src> may contain wildcards and matching will be done using Go’s filepath.Match rules.
    <src> must be relative to the source directory that is being built (the context of the build).
    <dest> is an absolute path, or a path relative to WORKDIR.
    If <dest> doesn’t exist, it is created along with all missing directories in its path.
    Reference - Best Practices

    `ENTRYPOINT`

    Usage:

    ENTRYPOINT ["<executable>", "<param1>", "<param2>"] (exec form, preferred)
    ENTRYPOINT <command> <param1> <param2> (shell form)
    Information:

    Allows you to configure a container that will run as an executable.
    Command line arguments to docker run <image> will be appended after all elements in an exec form ENTRYPOINT and will override all elements specified using CMD.
    The shell form prevents any CMD or run command line arguments from being used, but the ENTRYPOINT will start via the shell. This means the executable will not be PID 1 nor will it receive UNIX signals. Prepend exec to get around this drawback.
    Only the last ENTRYPOINT instruction in the Dockerfile will have an effect.
    Reference - Best Practices

    `VOLUME`

    Usage:

    VOLUME ["<path>", ...]
    VOLUME <path> [<path> ...]
    Creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers.

    Reference - Best Practices

    `USER`

    Usage:

    USER <username | UID>
    The USER instruction sets the user name or UID to use when running the image and for any RUN, CMD and ENTRYPOINT instructions that follow it in the Dockerfile.

    Reference - Best Practices

    `WORKDIR`

    Usage:

    WORKDIR </path/to/workdir>
    Information:

    Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, and ADD instructions that follow it.
    It can be used multiple times in the one Dockerfile. If a relative path is provided, it will be relative to the path of the previous WORKDIR instruction.
    Reference - Best Practices

    `ARG`

    Usage:

    ARG <name>[=<default value>]
    Information:

    Defines a variable that users can pass at build-time to the builder with the docker build command using the --build-arg <varname>=<value> flag.
    Multiple variables may be defined by specifying ARG multiple times.
    It is not recommended to use build-time variables for passing secrets like github keys, user credentials, etc. Build-time variable values are visible to any user of the image with the docker history command.
    Environment variables defined using the ENV instruction always override an ARG instruction of the same name.
    Docker has a set of predefined ARG variables that you can use without a corresponding ARG instruction in the Dockerfile.
    HTTP_PROXY and http_proxy
    HTTPS_PROXY and https_proxy
    FTP_PROXY and ftp_proxy
    NO_PROXY and no_proxy
    Reference

    `ONBUILD`

    Usage:

    ONBUILD <Dockerfile INSTRUCTION>
    Information:

    Adds to the image a trigger instruction to be executed at a later time, when the image is used as the base for another build. The trigger will be executed in the context of the downstream build, as if it had been inserted immediately after the FROM instruction in the downstream Dockerfile.
    Any build instruction can be registered as a trigger.
    Triggers are inherited by the "child" build only. In other words, they are not inherited by "grand-children" builds.
    The ONBUILD instruction may not trigger FROM, MAINTAINER, or ONBUILD instructions.
    Reference - Best Practices

    `STOPSIGNAL`

    Usage:

    STOPSIGNAL <signal>
    The STOPSIGNAL instruction sets the system call signal that will be sent to the container to exit. This signal can be a valid unsigned number that matches a position in the kernel’s syscall table, for instance 9, or a signal name in the format SIGNAME, for instance SIGKILL.

    Reference

    `HEALTHCHECK`

    Usage:

    HEALTHCHECK [<options>] CMD <command> (check container health by running a command inside the container)
    HEALTHCHECK NONE (disable any healthcheck inherited from the base image)
    Information:

    Tells Docker how to test a container to check that it is still working
    Whenever a health check passes, it becomes healthy. After a certain number of consecutive failures, it becomes unhealthy.
    The <options> that can appear are...
    --interval=<duration> (default: 30s)
    --timeout=<duration> (default: 30s)
    --retries=<number> (default: 3)
    The health check will first run interval seconds after the container is started, and then again interval seconds after each previous check completes. If a single run of the check takes longer than timeout seconds then the check is considered to have failed. It takes retries consecutive failures of the health check for the container to be considered unhealthy.
    There can only be one HEALTHCHECK instruction in a Dockerfile. If you list more than one then only the last HEALTHCHECK will take effect.
    <command> can be either a shell command or an exec JSON array.
    The command's exit status indicates the health status of the container.
    0: success - the container is healthy and ready for use
    1: unhealthy - the container is not working correctly
    2: reserved - do not use this exit code
    The first 4096 bytes of stdout and stderr from the <command> are stored and can be queried with docker inspect.
    When the health status of a container changes, a health_status event is generated with the new status.
    Reference

    `SHELL`

    Usage:

    SHELL ["<executable>", "<param1>", "<param2>"]
    Information:

    Allows the default shell used for the shell form of commands to be overridden.
    Each SHELL instruction overrides all previous SHELL instructions, and affects all subsequent instructions.
    Allows an alternate shell be used such as zsh, csh, tcsh, powershell, and others.


## Smaller Docker Images

To help make the images as small as possible, we can use `.dockerignore` to exclude files that we don't need. It helps in:

- Excluding secrets.
- Reduce image size with fewer not-needed files. 
- Reduce build cache invalidation due to log files changing. 


**Best Practices to Reduce Image Sizes & Build Times:**

- Use an official base image whenever possible
- Use variations of Alpine images when possible to keep your images lightweight.
- If using apt, combine RUN apt-get update with apt-get install in the same instruction to reduce number of layers to be built. Then chain multiple packages in that instruction. List the packages in alphabetical order over multiple lines with the \ character. For example:
RUN apt-get update && apt-get install -y \
    package-one \
    package-two 
 && rm -rf /var/lib/apt/lists/*
- Include `&& rm -rf /var/lib/apt/lists/*` at the end of the RUN instruction to clean up the apt cache so it isn’t stored in the layer.
- Use caching wisely by putting instructions likely to change lower in your Dockerfile.
- Use a `.dockerignore` file to keep unwanted and unnecessary files out of your image.


## CLI

`docker container my_command`

- create — Create a container from an image.
- start — Start an existing container.
- run — Create a new container and start it.
- ls — List running containers.
- inspect — See lots of info about a container.
- logs — Print logs.
- stop — Gracefully stop running container.
- kill —Stop main process in container abruptly.
- rm— Delete a stopped container.

`docker image my_command`

- build — Build an image.
- push — Push an image to a remote registry.
- ls — List images.
- history — See intermediate image info.
- inspect — See lots of info about an image, including the layers.
- rm — Delete an image.

`docker version` — List info about your Docker Client and Server versions.

`docker login` — Log in to a Docker registry.

`docker system prune` — Delete all unused containers, unused networks, and dangling images.

`docker container create my_repo/my_image:my_tag` - Create a container from an image.

`docker container create -a STDIN my_image`

- `-a` is short for --attach. Attach the container to STDIN, STDOUT or STDERR.

`docker container start my_container` — Start an existing container.

`docker container run my_image` — Create a new container and start it.

`docker container run -i -t -p 1000:8000 --rm my_image`

- `-i` is short for --interactive. Keep STDIN open even if unattached.
- `-t` is short for--tty. Allocates a pseudo terminal that connects your terminal with the container’s STDIN and STDOUT.
- `--rm` Automatically delete the container when it stops running.

`docker container inspect my_container` — See lots of info about a container.

`docker container logs my_container` — Print a container’s logs.

`docker container kill $(docker ps -q)` — Kill all running containers.

`docker image build -t my_repo/my_image:my_tag .` - Build a Docker image named my_image from the Dockerfile located at the specified path or URL.

`docker image push my_repo/my_image:my_tag` — Push an image to a registry.

`docker volume create`

`docker volume ls`

`docker volume inspect`

`docker volume rm`

`docker volume prune`

Common options for the --mount flag in `docker run --mount my_options my_image`:

- type=volume
- source=volume_name
- destination=/path/in/container
- readonly