pipeline {
    agent any

    stages {

        stage('Stop Old Container') {
            steps {
                bat 'docker stop job-tracker || exit 0'
                bat 'docker rm job-tracker || exit 0'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t job-tracker .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name job-tracker job-tracker'
            }
        }

    }
}