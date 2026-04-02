pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/PoojithaJuvva/job-tracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("job-tracker")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    docker.run("-d -p 5000:5000 job-tracker")
                }
            }
        }

    }
}