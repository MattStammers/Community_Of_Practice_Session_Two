## Getting started
1. Create a Docker Hub account
2. Install the Docker software on your system
3. Once your Docker application is running, open a shell (terminal) window, and run the following command to check that Docker is installed and the command line tools are working correctly.

```
 docker version
 ```

docker --version

## Basic Operations:

### 1. Pulling Images:
   - Use the `docker pull` command to download Docker images from a registry like Docker Hub:
     ```
     docker pull <image_name>
     ```

### 2. Running Containers:
   - Use the `docker run` command to start a container based on a Docker image:
     ```
     docker run <image_name>
     ```

### 3. Listing Containers:
   - Use the `docker ps` command to list running containers:
     ```
     docker ps
     ```

### 4. Stopping Containers:
   - Use the `docker stop` command to stop a running container:
     ```
     docker stop <container_id>
     ```

### 5. Removing Containers:
   - Use the `docker rm` command to remove a container:
     ```
     docker rm <container_id>
     ```

### 6. Building Images:
   - Use the `docker build` command to build a Docker image from a Dockerfile:
     ```
     docker build -t <image_name> <path_to_dockerfile>
     ```

### 7. Docker Compose:
   - Use the `docker-compose up` command to start a Docker Compose application:
     ```
     docker-compose up
     ```

## Build a Docker image
Basic commands: 
- FROM: Initialises the build and specifies the base image for subsequent instructions - all Dockerfiles start with this instruction.
- RUN: Runs a command (using /bin/sh on Linux).
- ADD: Copies new files, directories from and adds them to the filesystem of the image at the path .
- CMD: The default computational work that will be preformed when the container is executed using docker run. There can be only one CMD instruction in a Dockerfile.
- ENTRYPOINT: An ENTRYPOINT allows you to configure a container that will run as an executable. The best use for ENTRYPOINT is to set the image’s main command, allowing that image to be run as though it was that command (and then use CMD as the default flags).
- WORKDIR: The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile. If the WORKDIR doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction.
- COPY: Copy the current directory contents into the container.
- EXPOSE Make port 80 available to the world outside this container
- ENV: Define environment variable
