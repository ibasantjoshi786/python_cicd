pipeline {
    agent any
    stages {
        stage('Build, by activating the pelican conda environment') {
            steps {
                bat '''
                    echo stop the current process
                    call for /f "tokens=5" %a in ('netstat -ano ^| findstr :5000') do taskkill /F /PID %a
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
                    call set BUILD_NUMBER=771
                    call set JENKINS_SERVER_COOKIE=771
                    echo Deployment started...
                    set
                    call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat C:\\ProgramData\\Anaconda3\\envs\\pelican
                    call dir
                    call start /B start_flask.bat &
                    call set BUILD_ID=771
                    echo BUILD_ID is set to $BUILD_ID!
                    ping 127.0.0.1 -n 10 > nul
                '''
            }
        }
    }
}
