pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Vamsi9087/DevOps-Project-Two-Tier-Flask-App.git'
            }
        }

        stage('Build image') {
            steps {
                bat 'docker build -t flask-app .'
            }
        }

        stage('Deploy with docker compose') {
            steps {
                // Stop containers (ignore error if none running)
                bat 'docker compose down'

                // Start app and rebuild image
                bat 'docker compose up -d --build'
            }
        }
    }
}
