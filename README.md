DevOps Project Report: Automated CI/CD Pipeline for a 2-Tier Flask Application on AWS


1. Project Overview
This document outlines the step-by-step process for deploying a 2-tier web application (Flask + MySQL) on an AWS EC2 instance. The deployment is containerized using Docker and Docker Compose. A full CI/CD pipeline is established using Jenkins to automate the build and deployment process whenever new code is pushed to a GitHub repository.


2. Architecture Diagram

+-----------------+      +----------------------+      +-----------------------------+
|   Developer     |----->|     GitHub Repo      |----->|        Jenkins Server       |
| (pushes code)   |      | (Source Code Mgmt)   |      |  (on AWS EC2)               |
+-----------------+      +----------------------+      |                             |
                                                       | 1. Clones Repo              |
                                                       | 2. Builds Docker Image      |
                                                       | 3. Runs Docker Compose      |
                                                       +--------------+--------------+
                                                                      |
                                                                      | Deploys
                                                                      v
                                                       +-----------------------------+
                                                       |      Application Server     |
                                                       |      (Same AWS EC2)         |
                                                       |                             |
                                                       | +-------------------------+ |
                                                       | | Docker Container: Flask | |
                                                       | +-------------------------+ |
                                                       |              |              |
                                                       |              v              |
                                                       | +-------------------------+ |
                                                       | | Docker Container: MySQL | |
                                                       | +-------------------------+ |
                                                       +-----------------------------+



3. Step 1: AWS EC2 Instance Preparation
Launch EC2 Instance:
Navigate to the AWS EC2 console.
Launch a new instance using the Ubuntu 22.04 LTS AMI.
Select the t2.micro instance type for free-tier eligibility.
Create and assign a new key pair for SSH access.

<img width="1919" height="1098" alt="Screenshot 2026-01-16 130721" src="https://github.com/user-attachments/assets/c44a8ac1-3037-41ca-aef9-cc7e654341a4" />








