# ML Model Cloud Deployment
The project deploys a flask-based web application for a machine learning model to cloud and automates the whole process using a continuous integration tool.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
First off, there are two packages within the project: ```classification_model``` and ```ml_api```.

For each package, there is a ```requirements.txt``` within the package, which can be installed using following command:

```
pip install -r path/to/requirements.txt
```


### Installing
Please make sure you have ```requirements.txt``` installed as mentioned in **Prerequisites** before proceeding.

#### First, let's try to run everything locally and make sure they are working as expected. We'd perform following steps to do that:

Train and save the pipeline/model as a pickle object.

```
python path/to/run_training.py
```   




To access the model through the API, path to ```classification_model``` package is added to PYTHONPATH, so our API could import the package, and then use following commands to get the flask up and running:

```
set FLASK_APP=run.py
python run.py
```


<br>

**Testing**: To automate the tests for each package above, we'd run ```tests``` within each package as:  

```
pytest /path/to/tests
```

These tests try to predict the label for one of the data points, and check whether they are same as expected.


<br>  

#### Second, to deploy our application on AWS, we'd do it as following:

- To be able to access ```classfication_model``` package remotely from API, package needs to be hosted online.
  It's done as follows:
  A distribution package is created for the model using ```setup.py``` file. Following command creates the distribution package for us.

    ```
    python setup.py sdist bdist_wheel
    ``` 
    
<br>  



- Then distribution package is published to PyPI (Python Package Index). Since it's a learning project, I used a public package server.

    ```
    python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```  

   If the publishing of package was successful, you should find it on PyPI. Let's say the URL of the package server is ```PIP_EXTRA_INDEX_URL``` 
   e.g. ```PIP_EXTRA_INDEX_URL = "https://test.pypi.org/simple/"```  


<br>  



- Now that our package is online, we could create a docker image of the web application, which we would then deploy to AWS.
  We need to write a ```Dockerfile``` for this, which takes ```PIP_EXTRA_INDEX_URL``` as an argument.

  Docker image is built as follows:

    ```
    docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t ml_api:latest .
    ```    
    
    
<br>  



For the final few steps i.e. for deploying docker image to AWS, you should use AWS CLI, which can be configured with ```aws configure``` command. After configuring it, do following steps to upload docker image to AWS:  

- Tag the docker image

 ```
 docker tag ml-api:latest ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-2.amazonaws.com/ml-api:latest
 ```     


- Configure AWS ECR

 ```
 aws ecr get-login --no-include-email --region us-east-2
 ```   


- Upload docker image to ECR

 ```
 docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-2.amazonaws.com/ml-api:latest
 ```   


- Create an ECS cluster for the docker image uploaded to ECR, where we need to set environment variable ```PIP_EXTRA_INDEX_URL``` in addition to other configurations. Finishing this step will return an IP address of the website where our web application is being hosted.


<br><br>  

#### Finally, it's time to automate everything we've done so far, from training model to deploying it on AWS.
I used CircleCI for continuous integration which was linked to GitHub to access the project. While adding the project to CircleCI, it will create a config.yml to define the workflow which can be modified later as per need.

Now, every time a commit/empty-commit is made to the project, CircleCI will re-run the workflows to make sure everything is working as expected.



## Built with
- Flask
- Docker
- CircleCI
- AWS


## Acknowledgement
Project was inspired by Udemy Course :   https://www.udemy.com/course/deployment-of-machine-learning-models  
Course Instructor : Soledad Galli, Christopher Samiullah
