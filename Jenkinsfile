pipeline {
    agent any
    stages {
        stage('Deploy on ec2 instance') {
            steps {
                script {
                    // Copy file from 
                    bat '''
                        scp -r -i "E:\\Git Repo\\build_details\\python_cicd.pem" -v -o StrictHostKeyChecking=no "E:\\Git Repo\\build_details\\89\\report.xlsx" "ec2-user@54.149.67.232:/home/ec2-user"

                        echo Go into ec2 instance
                        ssh -i "E:\\Git Repo\\build_details\\python_cicd.pem" ec2-user@54.149.67.232 "cd 89 && setsid nohup python3 -m cicd_rnd.source.app > /dev/null 2>&1 &"
                    '''
                }
            }
        }
    }
} 
