pipeline {
    agent any

    environment {
        PROJECT_NAME = 'bits-website'
        DISCORD_WEBHOOK = credentials('discord-webhook')
        PROJECT_VERSION = get_version()
    }

    stages {
        stage('Docker Build') {
            steps {
                // build the docker image based on the Dockerfile and tag it with the build number
                // we use `-H ssh://jenkins@hogwarts` to connect to the docker daemon on hogwarts
                sh "docker -H ssh://jenkins@hogwarts build --no-cache -t ${PROJECT_NAME}:${PROJECT_VERSION} ."
            }
        }

       stage("Files Sync") {
            environment {
                WEBSITE_CONFIG = credentials('website-config')
                DEPLOY_FOLDER = get_container_name()
            }

            steps {
                // we copy the website to /var/bits-website which will then be mounted
                // to the docker container during the next stage. this way the files
                // stay easily accessible from the host.
                sh "ssh jenkins@hogwarts rm -rf /var/${DEPLOY_FOLDER}/*"
                sh 'cp $WEBSITE_CONFIG .'
                sh "rsync -av * jenkins@hogwarts:/var/${DEPLOY_FOLDER}/"
                // set group permissions so the directory will be writable to the container
                sh "ssh jenkins@hogwarts chgrp -R 1024 /var/${DEPLOY_FOLDER}/"
                sh "ssh jenkins@hogwarts chmod -R g+rw /var/${DEPLOY_FOLDER}/"
            }
       }

       stage ("Docker Deploy") {
            environment {
                CONTAINER_NAME = get_container_name()
                PORT = get_published_port()
            }

            steps {
                // we need to stop the container if it's already running. if it is not,
                // this will throw the error, so we need to catch it and tell jenkins
                // to mark it as successful anyways
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    sh "docker -H ssh://jenkins@hogwarts stop ${CONTAINER_NAME}"
                }
                // we also want to remove the container if it already exists
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    sh "docker -H ssh://jenkins@hogwarts rm ${CONTAINER_NAME}"
                }
                // now, start the container with the image we built in the last stage.
                // we mount the application folder from hogwarts to /app, give it a
                // suitable hostname and connect it to the hogwarts network.
                // the -d option runs the container in the background
                // the --rm option tells docker to remove the container after it stops
                sh "docker -H ssh://jenkins@hogwarts run -d --name ${CONTAINER_NAME} --mount source=${CONTAINER_NAME},target=/app --network hogwarts -p 127.0.0.1:${PORT}:5000/tcp ${PROJECT_NAME}:${PROJECT_VERSION}"
            }
       }
    }

    post {
        always {
            discordSend link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: DISCORD_WEBHOOK
        }
    }
}

def get_version() {
    if ("${BRANCH_NAME}" == 'master') {
        return "${BUILD_NUMBER}"
    } else {
        return "${BRANCH_NAME}-${BUILD_NUMBER}"
    }
}

def get_container_name() {
    if ("${BRANCH_NAME}" == 'master') {
        return "${PROJECT_NAME}"
    } else {
        return "${PROJECT_NAME}-dev"
    }
}

def get_published_port() {
    if ("${BRANCH_NAME}" == 'master') {
        return "5000"
    } else {
        return "5001"
    }
}
