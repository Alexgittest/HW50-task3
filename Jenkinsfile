pipeline {
//    triggers {
//        GenericTrigger (causeString: 'Generic Cause', regexpFilterExpression: '', regexpFilterText: '', token: 'task4-hw47', tokenCredentialId: '')
//              }
    agent any
    stages {
        stage('Git checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Alexgittest/Flaskapp.git'
				
            }
		}
		stage ('Docker build'){
			steps {
				script {
					docker.withRegistry('', 'dockerhub') {
						def Myflaskapp = docker.build("alexandrkorol/flaskapp:v3")
						Myflaskapp.push()
					}
				}
			}
		}
		stage ('slack send message'){
			steps {
				slackSend channel: '#jenkins', message: 'Docker build completed'
			}
		}
  }
}
