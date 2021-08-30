pipeline {
    agent any

    stages {
        stage("Master Uninstall") {
            when {
                branch 'master'
            }

            steps {
                sh """
                ssh jenkins@hogwarts << EOF
                    cd /var/flask/bits.team

                    echo "Closing website"
                    screen -X -S Website quit

                    echo "Wiping website directory"
                    rm -rf *
                    logout
                """
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
                sh 'cp $WEBSITE_CONFIG .'
                sh "rsync -av * jenkins@hogwarts:/var/flask/bits.team"
            }
       }

        stage("Master Deploy") {
            when {
                branch 'master'
            }

            steps {
                sh """
                    ssh jenkins@hogwarts << EOF
                      cd /var/flask/bits.team

                      echo "Creating venv"
                      python3 -m venv venv

                      echo "Sourcing venv"
                      source venv/bin/activate

                      echo "Installing pipenv"
                      pip install pipenv

                      echo "Syncing with Pipfile"
                      pipenv sync

                      echo "Starting server"
                      screen -dmS Website -d -m python3 waitress_server.py -h
                """

                sh "sleep 5"
                sh "ssh jenkins@hogwarts screen -list | grep -q '\\.Website'" // Test server went up successfully
            }
        }
    }

    post {
        always {
            discordSend link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: "https://discord.com/api/webhooks/861942609063706634/q7Hk_M2XtH2negfiYGws9EZuQEpUEw8FbCKhvy3PXl59a8qg_knBxsGfr8bP3LZORSkb"
        }
    }
}
