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
                    echo Deployment started...
                    call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat C:\\ProgramData\\Anaconda3\\envs\\pelican
                    call dir
                    start "Flask Server" /B python -m cicd_rnd.source.app
                    timeout /t 60 /nobreak
                '''
            }
        }
    }
}
