## HealthApp

### Description

This repository contains analysis done on log data from a health app which is a mobile application for Andriod devices. There are two ways to look at the analysis and they are as follows:
1. run the code blocks in `analysis.ipynb` notebook
2. run the dash app by running the `app.py`
3. run the dockerised version of the dash app by following the steps below

##### Steps to run the docker container for the dash app 
###### Setup and Running Instructions

This guide provides step-by-step instructions on how to set up and run the Player Analysis Dashboard using Docker.

###### Prerequisites
Before proceeding, ensure you have Docker installed on your system. If not, you can download and install Docker from [Docker's official website](https://docs.docker.com/get-docker/).

* Step 1: Build the Docker Container
First, you need to build the Docker container. Open your terminal or command prompt and run the following command:

```bash
docker build -t <name-of-container> .
```
Replace <name-of-container> with your desired container name. This command builds a Docker image based on the Dockerfile in the current directory.

* Step 2: Run the Docker Container
After building the image, you can run the container using:

```bash
docker run -p <port:port> <name-of-container>
```
Replace <port:port> with the desired port mapping (e.g., 8080:8080). The format is host-port:container-port. Ensure the port you choose is free on your host machine.

* Step 3: Access the Dashboard
Once the container is running, open a web browser and visit:

```makefile
localhost:<port>
```
Replace <port> with the host port you specified in the previous step. This will take you to the Player Analysis Dashboard.

#### Troubleshooting

If you encounter any issues, ensure that:

Docker is running on your system.
* The ports you specified are not being used by another service.
* The Dockerfile is correctly set up in your working directory.
* For more detailed Docker commands and troubleshooting, refer to the [Docker documentation](https://docs.docker.com/).


### Download
The raw logs are available for downloading at https://github.com/logpai/loghub.

### Citation
If you use this dataset from loghub in your research, please cite the following papers.
+ Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.# healthapp-log-analysis
