pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh '''#!/bin/bash
apt install nginx'''
      }
    }

    stage('test') {
      steps {
        echo 'testing done'
      }
    }

  }
}