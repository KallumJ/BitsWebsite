pipeline {
    agent any

    environment {
        PROJECT_NAME = 'bits-website'
        DISCORD_WEBHOOK = credentials('discord-webhook')
    }

    stages {
        stage('Docker Build') {
            when {
                branch 'master'
            }

            steps {
                // build the docker image based on the Dockerfile and tag it with the build number
                // we use `-H ssh://jenkins@hogwarts` to connect to the docker daemon on hogwarts
                sh "docker -H ssh://jenkins@hogwarts build --no-cache -t ${PROJECT_NAME}:${BUILD_NUMBER} ."
            }
        }

       stage("Master Sync") {
            when {
                 branch 'master'
            }

            environment {
                WEBSITE_CONFIG = credentials('website-config')
            }

            steps {
                // we copy the website to /var/bits-website which will then be mounted
                // to the docker container during the next stage. this way the files
                // stay easily accessible from the host.
                sh "ssh jenkins@hogwarts rm -rf /var/bits-website/*"
                sh 'cp $WEBSITE_CONFIG .'
                sh "rsync -av * jenkins@hogwarts:/var/bits-website/"
                // set group permissions so the directory will be writable to the container
                sh "ssh jenkins@hogwarts chgrp -R 1024 /var/bits-website/"
                sh "ssh jenkins@hogwarts chmod -R g+w /var/bits-website/"
            }
       }

       stage ("Docker Deploy") {
            when {
                 branch 'master'
            }

            steps {
                // we need to stop the container if it's already running. if it is not,
                // this will throw the error, so we need to catch it and tell jenkins
                // to mark it as successful anyways
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    sh "docker -H ssh://jenkins@hogwarts stop ${PROJECT_NAME}"
                }
                // we also want to remove the container if it already exists
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    sh "docker -H ssh://jenkins@hogwarts rm ${PROJECT_NAME}"
                }
                // now, start the container with the image we built in the last stage.
                // we mount the application folder from hogwarts to /app, give it a
                // suitable hostname and connect it to the hogwarts network.
                // the -d option runs the container in the background
                // the --rm option tells docker to remove the container after it stops
                sh "docker -H ssh://jenkins@hogwarts run -d --name ${PROJECT_NAME} --mount source=${PROJECT_NAME},target=/app --network hogwarts -p 127.0.0.1:5000:5000/tcp ${PROJECT_NAME}:${BUILD_NUMBER}"
            }
       }
    }

    post {
        always {
            discordSend link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: "$DISCORD_WEBHOOK"
        }
    }
}
