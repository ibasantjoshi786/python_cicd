pipeline {
    agent any
    stages {
        stage('Build, by activating the pelican conda environment') {
            steps {
                bat 'echo Building...'
                bat 'call C:\ProgramData\Anaconda3\condabin\activate.bat C:\ProgramData\Anaconda3\envs\pelican'
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
