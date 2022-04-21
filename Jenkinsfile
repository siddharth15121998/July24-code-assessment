pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh '''#!/bin/bash
sudo apt-get install nginx'''
      }
    }

    stage('test') {
      steps {
        echo 'testing done'
      }
    }

  }
}