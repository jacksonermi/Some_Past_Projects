# Week 6 Lab: Understanding the service running on Docker using Flask

**In this lab you will:** Learn containers and flask. Your ML application will eventually run, along with its API, in a container.  In this lab you will learn how to do this for a toy example. You will learn about two tools that need to be used:  Docker and Flask, and how they work together. 

**After the end of this lab you should:** know the contents and purpose of each of Dockerfile, Makefile, requirements.txt, master.yml and server.py in contributing to building a running service

In this Lab we will be using the specification file we have been developing since week 4 along with Flask, Python and Docker to explore some of the key aspects of our service. At this point we can create the service inside the virtual machine but today we will take more time to discuss the meaning of each of the files. Much of this will be review of the previous labs.

**Reminder** Use the example repo to get the working file structure, then copy those files to your repo, such that you can always go back to the example for a working example.

**AI help** The AI's will be providing feedback directly to your repos. So it is time to set up a project folder in your course repo. 

## Introducing the files

There are several file types in our application stucture. The week_6 directory in the student example repo shows the basic structure of our application. Following this structure keeps the files needed to create and describe the API are kept at the root level of the application. We have then added a src (source code directroy) that has all the python functions. We could add more directroties for data and any others we may need. This will mainatain the clean root application structure by only have the requried files (e.g., Dockerfile, Makfile etc., ) visible and the rest stored in diretories.

```
Application
 | Makefile
 | Dockerfile
 | requirements.txt
 | server.py
 | Readme.md
 |
 | src
 |   hello.py
 |   mult.py
 |   prediction.py
 |   sum.py
```


### /src

Contains all of our python functions

```
src
|    hello.py
|    mult.py
|    prediction.py
|    sum.py
```

We use directory structures to keep our application code clean.

### Makefile

Lets first take a look at what is all in the make docker-all command we have been using.

```bash
docker-all: docker-build docker-start
        @echo "Done"
```

The docker-all make command actually calls two commands. First the docker-build, the the docker-start. This is the typical process when creating containers. You first need to build the container by assigning it some requirements. These requriements describe the software components of the container, for example if the container needs python it needs to know to install python. One of the strenghts of containers are they are lightweight, but that means we need to know all the requirements our application needs to run, so we can build a container that satisfies them. These requirements are detailed in the Dokerfile, which is used when docker build is called.

```bash
docker-build:
	@echo: "building the image from dockerfile..."
	docker build -t e222/hello .
	@echo "image DONE"
```

The docker build command needs to be called at the root level of our application or at the same level as the Dockerfile, else you have to include a path to the Dockerfile within the build command.

### Dockerfile

Docker has pre-built images we can simply use to build our container. We will use the Ubuntu 18.04 base image, then build our python environment on top of that. In our case we are building a funcional linux OS within the container, there are lighter ways to build this application, however you would not be able to interact with the container as cleanly in these situations. The first line in the Dockerfile tell us the base of our build.

```bash
FROM ubuntu:18.04
```

The FROM statement is followed by a bunch of RUN statements. This is just like when you freshly install an OS onto any computer, you first must update the OS:

```bash
RUN apt-get update -y
```

Then install any development requirements, here we bring in additional OS tools and build our python 3.7 environment:

```bash
RUN apt-get install -y apt-utils
RUN apt-get install -y build-essential libssl-dev
RUN apt-get install -y git-core
RUN apt-get install -y dnsutils
RUN apt-get install -y curl
RUN apt install -y python3.7
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10
RUN update-alternatives --config python
RUN apt-get install -y python3.7-distutils
RUN apt-get install -y python3.7-dev
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install -U pip setuptools
RUN pip install psutil
```

We have built a fully functional development environment within our container, now we need to make a few connections.

**Discussuin Question: What OS are our VM's running? What is the difference between our VM and our Container?**

```bash
WORKDIR src/
COPY . /src
```

This above portion can be tricky, but WORKDIR defines our working directory within our **container**, if we were to enter our container we would see a directory called src. We then copy the conents of where we are currently located with the dot, COPY . /src. When we are sitting at the root level of our application using COPY . will copy all the conents of where I am into the src directroy within the container.

**Discussion Question: Where are you copying files from ?**

The port that our virtual machines are being exposed through is 11000, this is determined by the system admin of the physcial server our VM's are running on. We are running our service on local host (8080), shortly you will see how we are mapping the locally exposed container to the public 11000 which allows us to access through a browser. Circle back to the Makefile and see the docker-start portion. 

```bash
EXPOSE 11000
```

At this point we have a container that is ready for use. The one thing we are missing is the requirements to run our specific application. Think about this for a minute, if you were in production you could easily have any number of these containers ready to be built on demand. If developers create applications that can be run within this type of environment all the developer needs to supply are a specification file defining their endpoints, their python code and which pyhon libraries are required to run the application. For example if the application needs sci-kit learn libraries we need to make sure the container installs these. We do this using a file call requirements.txt. We can generate this file using the pip freeze command. 

**Discussion Point: Discuss pip freeze, and the use of ==, show example on github of vulnerabilities that can result from == and how we can avoid this.**

### requirements.txt

File containing the required python packages to run the service, this is generated from executing pip freeze in your development environment.

**Discussion Point: What happens if you dont have a clean development environment when you run pip freeze?**

### master.yml

OpenAPI 3.0 specification of the REST service, We spent week 4 on this with swaggerhub.

### server.py

Main function to start the Flask server, and define the root endpoint. You also see the line where we tell flask to use a specification file to describe the endpoints.  


## Flask and Docker

There are several tools used here.

[Flask](https://flask.palletsprojects.com/en/2.0.x/) is used to create the REST server containing your Python code. Once you start the flask server, you will be able to connect to your REST service via the browser and access the endpoints defined in the master.yml file.

**Discussion Points: Talk about HTTP requests, what requests have we used so far and what ones may be useful to us in the future**

[Docker](https://www.docker.com) is used to host this Flask REST application in a container instead of a local machine. There are various benefits of using containerization which your instructor will walk you through in class.

### Running the service (Hopefully review)

1. Navigate to the week_6 directory in the example student repo
2. Let's build the service.
```
make docker-build
```
3. Run the service
```
make docker-start
```
This will start up the docker container with the Flask REST service running inside it.

4. From the browser in your local machine, navigate to
```
vm-148-X.ise.luddy.indiana.edu:11000
```
Congratulations!, you should see a message coming from the service you hosted.

5. Try out the different endpoints we added
```
vm-148-X.ise.luddy.indiana.edu:11000/e222/hello
```
and
```
vm-148-X.ise.luddy.indiana.edu:11000/e222/sum/1/4
```

#### Cleaning up
Once you are done using the container, make sure to clean the environment using the following.

Stop the container
```
make docker-stop
```

Clean the docker environment
```
make docker-clean
```
 
### Student Task

This group work is meant to have the students learn about both Flask and Docker and for them to come up with an API endpoint that describes in detail Flask and Docker. The students can then share the endpoints and teach each other. 

Group A make a Flask endpoint.

Group B make a Docker endpoint.

These endpoints should tell the user important information about either Flask or Docker. Finally you should create an endpoint that tells the user what the ports used in this process are and state the HTTP/CRUD command being used for your endpoint/s.

**Instead of a Flask and Docker endpoint** the students were to create an endpoint that provides a description for their service. This will be progress towards the yaml checkpoint. 
