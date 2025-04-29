pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout stage'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Build Docker Image stage'
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                echo 'Push Docker Image to Docker Hub stage'
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
