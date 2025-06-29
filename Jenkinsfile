pipeline {
  agent any

  environment {
    PROJECT_NAME = 'app'
  }

  stages {
    stage('Clone Repository') {
      steps {
        dir('part2') {
          git branch: 'main', url: 'https://github.com/TahaAshfaq/DevOps.git'
        }
      }
    }

    stage('Extract Committer Email') {
      steps {
        dir('part2') {
          script {
            env.GIT_COMMITTER_EMAIL = sh(
              script: "git log -1 --pretty=format:'%ae'",
              returnStdout: true
            ).trim()
          }
        }
      }
    }
    
    stage('Test') {
      steps {
        script {
            sh 'docker-compose -p $PROJECT_NAME -f Dockercomposetest.yml down -v --remove-orphans || true'
            sh 'docker system prune -af || true'
            sh 'docker volume prune -f || true'
            sh 'docker-compose -p $PROJECT_NAME -f Dockercomposetest.yml up -d --build'
        }
      }
    }
    
    stage('Build and Deploy') {
      steps {
        script {
            sh 'docker-compose -p $PROJECT_NAME -f docker-compose.yml down -v --remove-orphans || true'
            sh 'docker system prune -af || true'
            sh 'docker volume prune -f || true'
            sh 'docker-compose -p $PROJECT_NAME -f docker-compose.yml up -d --build'
            sh 'docker-compose -p $PROJECT_NAME -f docker-compose.yml down -v --remove-orphans || true'
        }
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






