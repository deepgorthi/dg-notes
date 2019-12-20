# Docker Basics

## Install with script

[Link to script](https://get.docker.com/)
```bash
# Install steps can be skipped by using this script
    $ wget https://get.docker.com |sh
```

## Install

```bash
# Install Dependencies
    $ sudo yum install -y yum-utils device-mapper-persistent-data lvm2
# Add docker repo
    $ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# Install Docker community edition
    $ sudo yum install docker-ce
# Enable Docker service and start Docker
    $ sudo systemctl enable docker
    $ sudo systemctl start docker
```

??? "$ sudo docker run hello-world"
    ```bash
    # Run docker container 'hello-world'
        $ sudo docker run hello-world
            Unable to find image 'hello-world:latest' locally
            latest: Pulling from library/hello-world
            1b930d010525: Pull complete
            Digest: sha256:4fe721ccc2e8dc7362278a29dc660d833570ec2682f4e4194f4ee23e415e1064
            Status: Downloaded newer image for hello-world:latest

            Hello from Docker!
            This message shows that your installation appears to be working correctly.

            To generate this message, Docker took the following steps:
            1. The Docker client contacted the Docker daemon.
            2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
                (amd64)
            3. The Docker daemon created a new container from that image which runs the
                executable that produces the output you are currently reading.
            4. The Docker daemon streamed that output to the Docker client, which sent it
                to your terminal.

            To try something more ambitious, you can run an Ubuntu container with:
            $ docker run -it ubuntu bash

            Share images, automate workflows, and more with a free Docker ID:
            https://hub.docker.com/

            For more examples and ideas, visit:
            https://docs.docker.com/get-started/
    ```
```bash
# Giving cloud_user permissions to run docker by adding it to docker group
    $ sudo usermod -a -G docker cloud_user
    $ exit
    $ docker container run hello-world
```

## DockerHub and Docker repository

- `DockerHub` is analogous to `GitHub` where our code/docker-image is stored either privately or publicly.
- `Docker repo` is analogous to `RedHat repo` where it can either be created privately in an organization or use a public repo when needed.

Show docker images can be done either by `images` or `image ls` docker commands:
```bash
# Deprecated
$ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ubuntu              16.04               56bab49eef2e        2 weeks ago         123MB
    hello-world         latest              fce289e99eb9        11 months ago       1.84kB
#New command
$ docker image ls
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ubuntu              16.04               56bab49eef2e        2 weeks ago         123MB
    hello-world         latest              fce289e99eb9        11 months ago       1.84kB
```

Pull docker image:
```bash
$ docker pull ubuntu:16.04
    16.04: Pulling from library/ubuntu
    976a760c94fc: Extracting [===============================================>   ]  41.75MB/44.15MB
    c58992f3c37b: Download complete
    0ca0e5e7f12e: Download complete
    f2a274cc00ca: Download complete
```

Here is the dockerfile from Ubuntu [16.04 image](https://hub.docker.com/_/ubuntu)
??? "Ubuntu 16.04 dockerfile"
    ```dockerfile
    FROM scratch
    ADD ubuntu-xenial-core-cloudimg-amd64-root.tar.gz /
    # delete all the apt list files since they're big and get stale quickly
    RUN rm -rf /var/lib/apt/lists/*
    # this forces "apt-get update" in dependent images, which is also good
    # (see also https://bugs.launchpad.net/cloud-images/+bug/1699913)

    # a few minor docker-specific tweaks
    # see https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap
    RUN set -xe \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L40-L48
        && echo '#!/bin/sh' > /usr/sbin/policy-rc.d \
        && echo 'exit 101' >> /usr/sbin/policy-rc.d \
        && chmod +x /usr/sbin/policy-rc.d \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L54-L56
        && dpkg-divert --local --rename --add /sbin/initctl \
        && cp -a /usr/sbin/policy-rc.d /sbin/initctl \
        && sed -i 's/^exit.*/exit 0/' /sbin/initctl \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L71-L78
        && echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L85-L105
        && echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean \
        && echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean \
        && echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L109-L115
        && echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L118-L130
        && echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L134-L151
        && echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests

    # make systemd-detect-virt return "docker"
    # See: https://github.com/systemd/systemd/blob/aa0c34279ee40bce2f9681b496922dedbadfca19/src/basic/virt.c#L434
    RUN mkdir -p /run/systemd && echo 'docker' > /run/systemd/container

    CMD ["/bin/bash"]

    ```

To run the docker image, 
```bash
# deprecated
    $ docker run ubuntu:16.04
    $ docker run <ImageID>

# New command
    $ docker container run ubuntu:16.04
```

## Dockerfile

As an example, building a docker image with Ubuntu 16.04 as the base OS image, update the image to latest patches and install python3 on top of it. 

??? "Sample Dockerfile"
    ```dockerfile
    FROM ubuntu:16.04
    LABEL maintainer="deepgorthi@gmail.com"
    RUN apt-get update
    RUN apt-get install -y python3
    ```

## Building Docker image

To build the docker image, we need to run 
```bash
# '.' specifies to look for the dockerfile in the current directory
$ docker image build .
```
If the name of the dockerfile is different, we can build the image by doing 
```bash
$ docker image build <docker file name>
```

??? "Build output"
    ```bash
    $ docker image build .
        Sending build context to Docker daemon  2.048kB
        Step 1/4 : FROM ubuntu:16.04
        ---> 56bab49eef2e
        Step 2/4 : LABEL maintainer="deepgorthi@gmail.com"
        ---> Running in d76d48fb3f92
        Removing intermediate container d76d48fb3f92
        ---> 03b3755c4237
        Step 3/4 : RUN apt-get update
        ---> Running in 6b1995d3f8d0
        Get:1 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
        Get:2 http://security.ubuntu.com/ubuntu xenial-security InRelease [109 kB]
        Get:3 http://archive.ubuntu.com/ubuntu xenial-updates InRelease [109 kB]
        Get:4 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [1019 kB]
        Get:5 http://archive.ubuntu.com/ubuntu xenial-backports InRelease [107 kB]
        Get:6 http://archive.ubuntu.com/ubuntu xenial/main amd64 Packages [1558 kB]
        Get:7 http://security.ubuntu.com/ubuntu xenial-security/restricted amd64 Packages [12.7 kB]
        Get:8 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 Packages [593 kB]
        Get:9 http://security.ubuntu.com/ubuntu xenial-security/multiverse amd64 Packages [6280 B]
        Get:10 http://archive.ubuntu.com/ubuntu xenial/restricted amd64 Packages [14.1 kB]
        Get:11 http://archive.ubuntu.com/ubuntu xenial/universe amd64 Packages [9827 kB]
        Get:12 http://archive.ubuntu.com/ubuntu xenial/multiverse amd64 Packages [176 kB]
        Get:13 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [1396 kB]
        Get:14 http://archive.ubuntu.com/ubuntu xenial-updates/restricted amd64 Packages [13.1 kB]
        Get:15 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [996 kB]
        Get:16 http://archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [19.3 kB]
        Get:17 http://archive.ubuntu.com/ubuntu xenial-backports/main amd64 Packages [7942 B]
        Get:18 http://archive.ubuntu.com/ubuntu xenial-backports/universe amd64 Packages [8807 B]
        Fetched 16.2 MB in 3s (4134 kB/s)
        Reading package lists...
        Removing intermediate container 6b1995d3f8d0
        ---> 33e4e45672d8
        Step 4/4 : RUN apt-get install -y python3
        ---> Running in ac8388b43a00
        Reading package lists...
        Building dependency tree...
        Reading state information...
        The following additional packages will be installed:
        dh-python file libexpat1 libmagic1 libmpdec2 libpython3-stdlib
        libpython3.5-minimal libpython3.5-stdlib libsqlite3-0 libssl1.0.0
        mime-support python3-minimal python3.5 python3.5-minimal
        Suggested packages:
        libdpkg-perl python3-doc python3-tk python3-venv python3.5-venv
        python3.5-doc binutils binfmt-support
        The following NEW packages will be installed:
        dh-python file libexpat1 libmagic1 libmpdec2 libpython3-stdlib
        libpython3.5-minimal libpython3.5-stdlib libsqlite3-0 libssl1.0.0
        mime-support python3 python3-minimal python3.5 python3.5-minimal
        0 upgraded, 15 newly installed, 0 to remove and 4 not upgraded.
        Need to get 6436 kB of archives.
        After this operation, 33.2 MB of additional disk space will be used.
        Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libssl1.0.0 amd64 1.0.2g-1ubuntu4.15 [1084 kB]
        Get:2 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5-minimal amd64 3.5.2-2ubuntu0~16.04.9 [524 kB]
        Get:3 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libexpat1 amd64 2.1.0-7ubuntu0.16.04.5 [71.5 kB]
        Get:4 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3.5-minimal amd64 3.5.2-2ubuntu0~16.04.9 [1593 kB]
        Get:5 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-minimal amd64 3.5.1-3 [23.3 kB]
        Get:6 http://archive.ubuntu.com/ubuntu xenial/main amd64 mime-support all 3.59ubuntu1 [31.0 kB]
        Get:7 http://archive.ubuntu.com/ubuntu xenial/main amd64 libmpdec2 amd64 2.4.2-1 [82.6 kB]
        Get:8 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsqlite3-0 amd64 3.11.0-1ubuntu1.3 [397 kB]
        Get:9 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5-stdlib amd64 3.5.2-2ubuntu0~16.04.9 [2137 kB]
        Get:10 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3.5 amd64 3.5.2-2ubuntu0~16.04.9 [165 kB]
        Get:11 http://archive.ubuntu.com/ubuntu xenial/main amd64 libpython3-stdlib amd64 3.5.1-3 [6818 B]
        Get:12 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 dh-python all 2.20151103ubuntu1.2 [73.9 kB]
        Get:13 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3 amd64 3.5.1-3 [8710 B]
        Get:14 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libmagic1 amd64 1:5.25-2ubuntu1.3 [216 kB]
        Get:15 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 file amd64 1:5.25-2ubuntu1.3 [21.3 kB]
        debconf: delaying package configuration, since apt-utils is not installed
        Fetched 6436 kB in 2s (3013 kB/s)
        Selecting previously unselected package libssl1.0.0:amd64.
        (Reading database ... 4781 files and directories currently installed.)
        Preparing to unpack .../libssl1.0.0_1.0.2g-1ubuntu4.15_amd64.deb ...
        Unpacking libssl1.0.0:amd64 (1.0.2g-1ubuntu4.15) ...
        Selecting previously unselected package libpython3.5-minimal:amd64.
        Preparing to unpack .../libpython3.5-minimal_3.5.2-2ubuntu0~16.04.9_amd64.deb ...
        Unpacking libpython3.5-minimal:amd64 (3.5.2-2ubuntu0~16.04.9) ...
        Selecting previously unselected package libexpat1:amd64.
        Preparing to unpack .../libexpat1_2.1.0-7ubuntu0.16.04.5_amd64.deb ...
        Unpacking libexpat1:amd64 (2.1.0-7ubuntu0.16.04.5) ...
        Selecting previously unselected package python3.5-minimal.
        Preparing to unpack .../python3.5-minimal_3.5.2-2ubuntu0~16.04.9_amd64.deb ...
        Unpacking python3.5-minimal (3.5.2-2ubuntu0~16.04.9) ...
        Selecting previously unselected package python3-minimal.
        Preparing to unpack .../python3-minimal_3.5.1-3_amd64.deb ...
        Unpacking python3-minimal (3.5.1-3) ...
        Selecting previously unselected package mime-support.
        Preparing to unpack .../mime-support_3.59ubuntu1_all.deb ...
        Unpacking mime-support (3.59ubuntu1) ...
        Selecting previously unselected package libmpdec2:amd64.
        Preparing to unpack .../libmpdec2_2.4.2-1_amd64.deb ...
        Unpacking libmpdec2:amd64 (2.4.2-1) ...
        Selecting previously unselected package libsqlite3-0:amd64.
        Preparing to unpack .../libsqlite3-0_3.11.0-1ubuntu1.3_amd64.deb ...
        Unpacking libsqlite3-0:amd64 (3.11.0-1ubuntu1.3) ...
        Selecting previously unselected package libpython3.5-stdlib:amd64.
        Preparing to unpack .../libpython3.5-stdlib_3.5.2-2ubuntu0~16.04.9_amd64.deb ...
        Unpacking libpython3.5-stdlib:amd64 (3.5.2-2ubuntu0~16.04.9) ...
        Selecting previously unselected package python3.5.
        Preparing to unpack .../python3.5_3.5.2-2ubuntu0~16.04.9_amd64.deb ...
        Unpacking python3.5 (3.5.2-2ubuntu0~16.04.9) ...
        Selecting previously unselected package libpython3-stdlib:amd64.
        Preparing to unpack .../libpython3-stdlib_3.5.1-3_amd64.deb ...
        Unpacking libpython3-stdlib:amd64 (3.5.1-3) ...
        Selecting previously unselected package dh-python.
        Preparing to unpack .../dh-python_2.20151103ubuntu1.2_all.deb ...
        Unpacking dh-python (2.20151103ubuntu1.2) ...
        Processing triggers for libc-bin (2.23-0ubuntu11) ...
        Setting up libssl1.0.0:amd64 (1.0.2g-1ubuntu4.15) ...
        debconf: unable to initialize frontend: Dialog
        debconf: (TERM is not set, so the dialog frontend is not usable.)
        debconf: falling back to frontend: Readline
        debconf: unable to initialize frontend: Readline
        debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.22.1 /usr/local/share/perl/5.22.1 /usr/lib/x86_64-linux-gnu/perl5/5.22 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.22 /usr/share/perl/5.22 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
        debconf: falling back to frontend: Teletype
        Setting up libpython3.5-minimal:amd64 (3.5.2-2ubuntu0~16.04.9) ...
        Setting up libexpat1:amd64 (2.1.0-7ubuntu0.16.04.5) ...
        Setting up python3.5-minimal (3.5.2-2ubuntu0~16.04.9) ...
        Setting up python3-minimal (3.5.1-3) ...
        Processing triggers for libc-bin (2.23-0ubuntu11) ...
        Selecting previously unselected package python3.
        (Reading database ... 5757 files and directories currently installed.)
        Preparing to unpack .../python3_3.5.1-3_amd64.deb ...
        Unpacking python3 (3.5.1-3) ...
        Selecting previously unselected package libmagic1:amd64.
        Preparing to unpack .../libmagic1_1%3a5.25-2ubuntu1.3_amd64.deb ...
        Unpacking libmagic1:amd64 (1:5.25-2ubuntu1.3) ...
        Selecting previously unselected package file.
        Preparing to unpack .../file_1%3a5.25-2ubuntu1.3_amd64.deb ...
        Unpacking file (1:5.25-2ubuntu1.3) ...
        Processing triggers for libc-bin (2.23-0ubuntu11) ...
        Setting up mime-support (3.59ubuntu1) ...
        Setting up libmpdec2:amd64 (2.4.2-1) ...
        Setting up libsqlite3-0:amd64 (3.11.0-1ubuntu1.3) ...
        Setting up libpython3.5-stdlib:amd64 (3.5.2-2ubuntu0~16.04.9) ...
        Setting up python3.5 (3.5.2-2ubuntu0~16.04.9) ...
        Setting up libpython3-stdlib:amd64 (3.5.1-3) ...
        Setting up libmagic1:amd64 (1:5.25-2ubuntu1.3) ...
        Setting up file (1:5.25-2ubuntu1.3) ...
        Setting up python3 (3.5.1-3) ...
        running python rtupdate hooks for python3.5...
        running python post-rtupdate hooks for python3.5...
        Setting up dh-python (2.20151103ubuntu1.2) ...
        Processing triggers for libc-bin (2.23-0ubuntu11) ...
        Removing intermediate container ac8388b43a00
        ---> a41c41ef3ce9
        Successfully built a41c41ef3ce9
    ```

## Running the Container

To run the image in a docker container,
```bash
$ docker image ls
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    <none>              <none>              a41c41ef3ce9        11 minutes ago      186MB
    ubuntu              16.04               56bab49eef2e        2 weeks ago         123MB
    hello-world         latest              fce289e99eb9        11 months ago       1.84kB

$ docker container run -i -t --name python-container a41 
# just enough chars are enough to distinguish between docker images
# -i is short for --interactive. Keep STDIN open even if unattached.
# -t is short for--tty. Allocates a pseudo terminal that connects your terminal with the container’s STDIN and STDOUT.
# You need to specify both -i and -t to then interact with the container through your terminal shell.
```

A container stops after exiting from the command line of that container. 

List of running containers:
```bash
$ docker container ls
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    e365eb0e4568        a41                 "/bin/bash"         42 seconds ago      Up 40 seconds                           python-container_v2
```
List of all stopped and running containers:
```bash
$ docker container ls -a
    CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS                      PORTS               NAMES
    e365eb0e4568        a41                 "/bin/bash"         About a minute ago   Up About a minute                               python-container_v2
    11087b710633        a41                 "/bin/bash"         11 minutes ago       Exited (0) 4 minutes ago                        python-container
    db3e7658a34b        ubuntu:16.04        "/bin/bash"         35 minutes ago       Exited (0) 34 minutes ago                       cool_beaver
    b6fd3fb58e5a        hello-world         "/hello"            6 hours ago          Exited (0) 6 hours ago                          hardcore_pascal
    167b6f3834e0        hello-world         "/hello"            6 hours ago          Exited (0) 6 hours ago                          boring_hellman
```

Starting and stopping a container without running the shell or logging in:
```bash
$ docker container start python-container
    python-container
$ docker container ls
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    11087b710633        a41                 "/bin/bash"         14 minutes ago      Up 24 seconds                           python-container
$ docker container stop python-container
    python-container
$ docker container ls
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

After starting up a container using `start`, to attach to that container, we can run:
```bash
$ docker container attach <container ID>
root@11087b710633:/#
```

## Removing Containers (rm)

```bash
$ docker container ls -a
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
    e365eb0e4568        a41                 "/bin/bash"         10 minutes ago      Exited (0) 6 minutes ago                        python-container_v2
    11087b710633        a41                 "/bin/bash"         20 minutes ago      Exited (0) 7 seconds ago                        python-container
    db3e7658a34b        ubuntu:16.04        "/bin/bash"         43 minutes ago      Exited (0) 43 minutes ago                       cool_beaver
    b6fd3fb58e5a        hello-world         "/hello"            6 hours ago         Exited (0) 6 hours ago                          hardcore_pascal
    167b6f3834e0        hello-world         "/hello"            6 hours ago         Exited (0) 6 hours ago                          boring_hellman
$ docker container rm 167b6f3834e0
    167b6f3834e0
$ docker container rm hardcore_pascal
    hardcore_pascal
$ docker container rm db3e7658a34b python-container python-container_v2
    db3e7658a34b
    python-container
    python-container_v2
$ docker container ls -a
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
## Removing Images
```bash
$ docker image ls
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    <none>              <none>              a41c41ef3ce9        34 minutes ago      186MB
    ubuntu              16.04               56bab49eef2e        2 weeks ago         123MB
    hello-world         latest              fce289e99eb9        11 months ago       1.84kB
$ docker image rm fce289e99eb9
    Untagged: hello-world:latest
    Untagged: hello-world@sha256:4fe721ccc2e8dc7362278a29dc660d833570ec2682f4e4194f4ee23e415e1064
    Deleted: sha256:fce289e99eb9bca977dae136fbe2a82b6b7d4c372474c9235adc1741675f587e
    Deleted: sha256:af0b15c8625bb1938f1d7b17081031f649fd14e6b233688eea3c5483994a66a3
```

## Pushing image to Docker repo 

To login to docker:
```bash
$ docker login
    Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
    Username: deepgorthi
    Password:
    WARNING! Your password will be stored unencrypted in /home/cloud_user/.docker/config.json.
    Configure a credential helper to remove this warning. See
    https://docs.docker.com/engine/reference/commandline/login/#credentials-store

    Login Succeeded
```

Tag the image that will be pushed to docker repo and push it:
```bash
$ docker image ls
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    <none>              <none>              a41c41ef3ce9        37 minutes ago      186MB
    ubuntu              16.04               56bab49eef2e        2 weeks ago         123MB

$ docker image tag a41c41ef3ce9 deepgorthi/ubu-python3

$ docker image ls
    REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
    deepgorthi/ubu-python3   latest              a41c41ef3ce9        38 minutes ago      186MB
    ubuntu                   16.04               56bab49eef2e        2 weeks ago         123MB

$ docker image push deepgorthi/ubu-python3
    The push refers to repository [docker.io/deepgorthi/ubu-python3]
    fc529f7b8eec: Pushed
    c992de3f99a0: Pushed
    aa7f8c8d5f39: Mounted from library/ubuntu
    48817fbd6c92: Mounted from library/ubuntu
    1b039d138968: Mounted from library/ubuntu
    7082d7d696f8: Mounted from library/ubuntu
    latest: digest: sha256:f348584be25aa65a0d266d77eadfeaad955385736462cea5efd68d1a4473760d size: 1574
```

!!! info "Links"
    - [List of Docker commands](https://geekflare.com/docker-commands/)
    - [VMs, Containers and Docker](https://www.freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b/)
    - Learn enough useful Docker series
        - [Part 1](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b)
        - [Part 2](https://towardsdatascience.com/learn-enough-docker-to-be-useful-1c40ea269fa8)
        - [Part 3](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b0b44222eef5)
        - [Part 4](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e)
        - [Part 5](https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421)
        - [Part 6](https://towardsdatascience.com/pump-up-the-volumes-data-in-docker-a21950a8cd8)