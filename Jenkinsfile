pipeline {
    agent any
    stages {
        stage('Build, by activating the pelican conda environment') {
            steps {
                bat '''
                    echo Building...
                    call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat C:\\ProgramData\\Anaconda3\\envs\\pelican
                    call python --version
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                    echo Testing...
                    call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat C:\\ProgramData\\Anaconda3\\envs\\pelican
                    call python --version
                    call pytest
                '''
                
                // Add your test commands here
            }
        }
        stage('Deploy') {
            steps {
                input "Do you want to deploy the application"
                bat '''
                    echo Deployment started...
                    call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat C:\\ProgramData\\Anaconda3\\envs\\pelican
                    call dir
                    call python calculator.py
                '''
            }
        }
    }
}
