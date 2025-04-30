pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE_NAME = "excommunicades/devops_django7"
        GITHUB_CREDENTIALS = credentials('github-token')
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Cloning the repository...'
                    git credentialsId: 'github-token', url: 'https://github.com/excommunicades/DevOps_Django.git'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    docker.build(DOCKER_IMAGE_NAME, 'DevOpsDjango/')
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    echo 'Pushing Docker image to Docker Hub...'
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image(DOCKER_IMAGE_NAME).push()
                    }
                }
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
