pipeline {
    agent any
    stages {
        stage('Build, by activating the pelican conda environment') {
            steps {
                bat '''
                    echo stop the current process
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
                    call set BUILD_NUMBER=dontKillMe
                    call set BUILD_ID=dontKillMe
                    call set JENKINS_SERVER_COOKIE=dontKillMe
                    call set JENKINS_NODE_COOKIE=dontKillMe
                    echo Deployment started...
                    call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat C:\\ProgramData\\Anaconda3\\envs\\pelican
                    call terminate_flask.bat
                    call start /B start_flask.bat &
                '''
            }
        }
    }
}
