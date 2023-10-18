pipeline {
    agent any
    stages {
        stage('Build, by activating the pelican conda environment') {
            steps {
                bat 'echo Building...'
                bat 'call activate pelican'
                // Add your build commands here
            }
        }
        stage('Test') {
            steps {
                bat 'echo Testing...'
                // Add your test commands here
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deployment...'
                // Add your deployment commands here
            }
        }
    }
}
