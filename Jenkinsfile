// pipeline {
//   agent any

//   environment {
//     PROJECT_NAME = 'app'
//   }

//   stages {
//     stage('Clone Repository') {
//       steps {
//         dir('part2') {
//           git branch: 'main', url: 'https://github.com/TahaAshfaq/DevOps.git'
//         }
//       }
//     }
    
//     stage('Build and Deploy') {
//       steps {
//         script {
//             sh 'docker-compose -p $PROJECT_NAME -f docker-compose.yml down -v --remove-orphans || true'
//             sh 'docker system prune -af || true'
//             sh 'docker volume prune -f || true'
//             sh 'docker-compose -p $PROJECT_NAME -f docker-compose.yml up -d --build'
//         }
//       }
//     }

//   }
// }





pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'selenium-tests'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/TahaAshfaq/DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t selenium-tests .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'docker run selenium-tests'
            }
        }
    }

    post {
        always {
            mail to: "${GIT_COMMITTER_EMAIL}",
                 subject: "DevOps Selenium Test Results",
                 body: "The Jenkins pipeline has finished running the Selenium tests. Check Jenkins logs for details."
        }
    }
}
