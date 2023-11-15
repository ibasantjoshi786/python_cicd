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
                    call pytest --excelreport=report.xlsx
                    set build_no=%BUILD_NUMBER%
                    call mkdir "E:\\Git Repo\\build_details\\%build_no%"
                    call copy "report.xlsx" "E:\\Git Repo\\build_details\\%build_no%\\report.xlsx"
                    del report.xlsx
                    call xcopy * "E:\\Git Repo\\build_details\\%build_no%" /E /H /C /I
                '''
                
                // Add your test commands here
            }
        }
        stage('Deploy Locally') {
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

        stage('Deploy on ec2 instance') {
            steps {
                script {
                    // Copy file from 
                    bat '''
                        scp -r -i "E:\\Git Repo\\build_details\\python_cicd.pem" -v -o StrictHostKeyChecking=no "E:\\Git Repo\\build_details\\89" "ec2-user@54.149.67.232:/home/ec2-user"

                        echo Go into ec2 instance
                        ssh -i "E:\\Git Repo\\build_details\\python_cicd.pem" ec2-user@54.149.67.232

                        echo Start the python server
                        cd 89
                        nohup python3 -m cicd_rnd.source.app &
                    '''
                }
            }
        }
    }
}
