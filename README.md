DevOps Project Report: Automated CI/CD Pipeline for a 2-Tier Flask Application on AWS


1. Project Overview
This document outlines the step-by-step process for deploying a 2-tier web application (Flask + MySQL) on an AWS EC2 instance. The deployment is containerized using Docker and Docker Compose. A full CI/CD pipeline is established using Jenkins to automate the build and deployment process whenever new code is pushed to a GitHub repository.


2. Architecture Diagram
3. 
  
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


 2) **Configure Security Group:
Create a security group with the following inbound rules:
Type: SSH, Protocol: TCP, Port: 22, Source: Your IP
Type: HTTP, Protocol: TCP, Port: 80, Source: Anywhere (0.0.0.0/0)
Type: Custom TCP, Protocol: TCP, Port: 5000 (for Flask), Source: Anywhere (0.0.0.0/0)
Type: Custom TCP, Protocol: TCP, Port: 8080 (for Jenkins), Source: Anywhere (0.0.0.0/0)**



3)Connect to EC2 Instance:
Use SSH to connect to the instance's public IP address.
    ssh -i /path/to/key.pem ubuntu@<ec2-public-ip>


    . Step 2: Install Dependencies on EC2
Update System Packages:

sudo apt update && sudo apt upgrade -y
Install Git, Docker, and Docker Compose:

sudo apt install git docker.io docker-compose-v2 -y
Start and Enable Docker:

sudo systemctl start docker
sudo systemctl enable docker
Add User to Docker Group (to run docker without sudo):

sudo usermod -aG docker $USER
newgrp docker
5. Step 3: Jenkins Installation and Setup
Install Java (OpenJDK 17):

sudo apt install openjdk-17-jdk -y
Add Jenkins Repository and Install:

curl -fsSL [https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key](https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key) | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] [https://pkg.jenkins.io/debian-stable](https://pkg.jenkins.io/debian-stable) binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null


sudo apt update
sudo apt install jenkins -y
Start and Enable Jenkins Service:

sudo systemctl start jenkins
sudo systemctl enable jenkins
Initial Jenkins Setup:

Retrieve the initial admin password:
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
Access the Jenkins dashboard at http://<ec2-public-ip>:8080.
Paste the password, install suggested plugins, and create an admin user.
Grant Jenkins Docker Permissions:

sudo usermod -aG docker jenkins
sudo systemctl restart jenkins









