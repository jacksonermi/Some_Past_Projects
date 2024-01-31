------------------------------------------------------------------------Final Project---------------------------------------------------------------------------

1. What does the project do?
The project demonstrates a volumized container as a means to host a website and machine learning model which users can access and gain accurate predictions based on the upload of a csv file. However, this is only one of the endpoints in our API, there also exists three other. One for printing the classfiication report of the test dataset, one for printing the confusion matrix of the dataset, and one for manually inputting a datapoint as opposed to using a csv file. 

2. Why is the project useful?
The project allows for the introduction into the construction of API frameworks; the architecture, construction, and maintaining of a volumized container; the function/use of a virtual machine (or VM for short); further machine learning model development; as well as a taste of how we as intelligent systems engineers might use our abilities to greater effect in the future. 

3. How can users get started with the project?
This depends on how you intend to use the project. If you intend on looking at it from a user perspective, you need only access the url for the website hosted on SwaggerHub to utilize the classification model. Conversely, if you are intending on running this code as a developer, I would reccomend first looking at the docker file and make file to better understand how to construct the volumized container. You may be required to install DockerHub locally if you do not already have it. Actually building the environment (or container) for our system is actually only one line of code 'make docker-all'. This line is again defined in the makefile.

4. Where can users get help with the project?
There exists another readme inside the actual project repo itself which contains a more detailed and nuanced description of some of the main files in the repository. Here's a brief description of the big ones: 
Dockerfile: Creates the container. Boots a new os (in our case) and exposes the port for the container to reference.
Makefile: Creates a list of user defined functions that can be used to run multiple lines of bash(console) commands.
Server.py: Python file that loads our api and expresses endpoints(does this through the master.yml file and the Flask library).
master.yml: Defines the endpoints of our api
Bean_mdl_project.ipynb: The notebook we used to train our models
bean_mdl.pkl: our trained mdl
requirements.txt: Has a list of dependencies that are to be installed on the container.

5. Who maintains and contributes to the project?
This project is officially complete, it was more of a technique to aid us in our studies as we train to become more well rounded and capable engineers as opposed to a system that will be deployed in an actual work environment. That being said, it will be a great tool to refer back to in the future.

