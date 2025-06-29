pipeline {
  agent any

  environment {
    PROJECT_NAME = 'app'
    EMAIL_BODY = ''
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
            // Wait for selenium-tests container to finish
            sh 'docker wait selenium-test-runner'
            // Print test logs to Jenkins console
            sh 'docker logs selenium-test-runner || true'
            // Capture exit code and fail build if tests failed
            def exitCode = sh(script: 'docker inspect selenium-test-runner --format="{{.State.ExitCode}}"', returnStdout: true).trim()
            if (exitCode != '0') {
                currentBuild.result = 'FAILURE'
                env.EMAIL_BODY = 'The Jenkins pipeline has finished running the Selenium tests. Some tests FAILED. Check Jenkins logs for details.'
                error("Tests failed. Exit code: ${exitCode}")
            } else {
                env.EMAIL_BODY = 'The Jenkins pipeline has finished running the Selenium tests. All tests PASSED. Check Jenkins logs for details.'
            }
            sh 'docker-compose -p $PROJECT_NAME -f Dockercomposetest.yml down -v --remove-orphans || true'
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
        }
      }
    }


  }
  post {
        always {
            script {
                def body = env.EMAIL_BODY ?: 'The Jenkins pipeline has finished running. Check Jenkins logs for details.'
                mail to: "${GIT_COMMITTER_EMAIL}",
                     subject: "DevOps Selenium Test Results",
                     body: body
            }
        }
    }
}






