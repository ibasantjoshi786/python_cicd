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
                    // Define EC2 instance details
                    def ec2Host = '10.1.65.115'
                    def ec2User = 'root'
                    def remoteDir = '/root/cicd'
                    def localDir = '.'
                    def pscpExe = '"C:\\Program Files (x86)\\PuTTY\\pscp.exe"'
                    
                    // Retrieve the host key and add it to known_hosts
                    def sshKeyScanCmd = """ssh-keyscan ${ec2Host} >> ~/.ssh/known_hosts"""
                    bat "cmd /c ${sshKeyScanCmd}"
            
                    // Define deployment commands
                    def deployCmd = """pscp -l ${ec2User} -pw Admin@cat2021 -r ${localDir} ${ec2Host}:${remoteDir}"""
            
                    // Execute deployment command
                    bat "cmd /c ${deployCmd}"
                }
            }
        }
    }
}
