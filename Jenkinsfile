pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Vamsi9087/DevOps-Project-Two-Tier-Flask-App.git'
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t two-tier-flask-app .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker-compose down || exit 0'
                bat 'docker-compose up -d --build'
            }
        }
    }
}
