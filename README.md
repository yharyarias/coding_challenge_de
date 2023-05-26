<a name="readme"></a>

[![Forks][forks-shield]][forks-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/yharyarias/coding_challenge_de">
    <img src="images/logo.png" alt="Logo" width="600" height="100">
  </a>

  <h3 align="center">Globant’s Data Engineering Coding Challenge</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#installation">Section 1: API</a></li>
        <li><a href="#installation">Section 2: SQL</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- GETTING STARTED -->
# GETTING STARTED

This project consists in the creation of an API that receives a csv extension file. A pipeline was created in which the data is preprocessed, that is to say, it is cleaned before sending it to a MySQL database hosted in GCP. After the data is sent, the API is dockerized to deploy it in GCP.
Below are the instructions and requirements to execute the project.


### Prerequisites

Before starting it is necessary to create a virtual environment, it is recommended to do it with PIPENV, located in the root of the project. The following command will generate the environment automatically.

* shell
  ```sh
  pipenv shell
  ```

Download the packages from the requirements.txt file
* shell
  ```sh
  pip install -r requirements.txt
  ```
## RUN API
It is time to run the API, first we will test it locally then on GCP
* shell
  ```sh
  uvicorn main:app --reload
  ```
## Run Docker container 
You can also run the container where the API is stored (should work the same as running the API directly).
* shell
  ```sh
  uvicorn main:app --reload
  ```


<!-- ABOUT THE PROJECT -->
## About The Project

You will find several different sections in here. Mind that:
* You can choose which sections to solve based on your experience and available time
* if you don’t know how to solve a section, you can proceed with the following one
* You can use whichever language, libraries, and frameworks that you want.
* The usage of cloud services is allowed, you can choose whichever cloud provider that
you want
* Try to always apply best practices and develop a scalable solution.
* We recommend you to solve everything
* If you don’t have time to solve any sections, try to think the toolstack you would like to
use and the resulting architecture, and why.
* Every complement you might want to add is highly welcome!
* In case you have a personal github repository to share with the interviewer, please do

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Section 1: API

In the context of a DB migration with 3 different tables (departments, jobs, employees) , create a local REST API that must:
1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request
You need to publish your code in GitHub. It will be taken into account if frequent updates are made to the repository that allow analyzing the development process. Ideally, create a markdown file for the Readme.md

Clarifications
* You decide the origin where the CSV files are located.
* You decide the destination database type, but it must be a SQL database.
* The CSV file is comma separated.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Section 2: SQL

You need to explore the data that was inserted in the previous section. The stakeholders ask for some specific metrics they need. You should create an end-point for each requirement.

## Requirements
* Number of employees hired for each job and department in 2021 divided by quarter. The table must be ordered alphabetically by department and job.
* List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in 2021 for all the departments, ordered by the number of employees hired (descending).

# Bonus Track! Cloud, Testing & Containers

Add the following to your solution to make it more robust:
* Host your architecture in any public cloud (using the services you consider more
adequate)
* Add automated tests to the API
* You can use whichever library that you want
* Different tests types, if necessary, are welcome 
* Containerize your application
* Create a Dockerfile to deploy the package

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Yhary Arias - [@yharyarias](https://www.linkedin.com/in/yharyarias/)

Email: yharystefa@gmail.com

Bucaramanga, Colombia

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- REFERENCES -->
## References

[Google Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run?hl=es-419)
[Dockerfile](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
[FastAPI](https://fastapi.tiangolo.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>