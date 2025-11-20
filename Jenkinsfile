pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/IanMQ/PC2api.git'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t api-tierra:latest .'
            }
        }

        stage('Detener contenedor previo') {
            steps {
                sh 'docker rm -f api-tierra || true'
            }
        }

        stage('Ejecutar contenedor nuevo') {
            steps {
                sh 'docker run -d -p 8000:8000 --name api-tierra api-tierra:latest'
            }
        }
    }
}
