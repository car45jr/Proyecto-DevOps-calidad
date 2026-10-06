pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Obteniendo el código fuente del repositorio...'
                checkout scm
            }
        }

        stage('Instalar Dependencias') {
            steps {
                echo 'Instalando dependencias desde requirements.txt...'
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar Pruebas Automatizadas') {
            steps {
                echo 'Ejecutando pruebas unitarias con pytest...'
                sh 'pytest -v'
            }
        }

        stage('Medir Cobertura') {
            steps {
                echo 'Generando reporte de cobertura de código...'
                sh 'pytest --cov=app --cov-report=term-missing --cov-report=xml'
            }
        }
    }

    post {
        always {
            echo 'Finalización del pipeline de Jenkins.'
        }
        success {
            echo '¡Pipeline exitoso! Todas las pruebas pasaron satisfactoriamente.'
        }
        failure {
            echo '¡Pipeline fallido! Se detectaron errores en las pruebas automatizadas.'
        }
    }
}
