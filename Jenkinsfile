pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Medir cobertura') {
            steps {
                bat 'python -m pytest --cov=app --cov-report=term-missing --cov-report=xml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente.'
        }
        failure {
            echo 'Se detectaron errores durante las pruebas.'
        }
    }
}