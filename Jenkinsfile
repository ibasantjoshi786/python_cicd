pipeline {
    agent any
    stages {
        stage('Build, by activating the pelican conda environment') {
            steps {
                bat '''
                    echo Building...
                    call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat C:\\ProgramData\\Anaconda3\\envs\\pelican
                    call python --version
                    call python -m cicd_rnd.test_suite.test_calculator
                '''
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
