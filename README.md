Below commands can be executed to check the execution
38  gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker     --location=us-west2 --description="Docker repository"
39  gcloud artifacts repositories list
40  gcloud config get-value project
41  gcloud builds submit --region=us-west2 --tag us-west2-docker.pkg.dev/peerless-sensor-414405/quickstart-docker-repo/quickstart-image:tag1
42  gcloud run deploy --image us-west2-docker.pkg.dev/peerless-sensor-414405/quickstart-docker-repo/quickstart-image:tag1 --platform managed --no-allow-unauthenticated --region us-west2 test-service
Testing using
curl -X GET https://test-service-usai435zsq-wl.a.run.app
71  curl -X POST  https://test-service-usai435zsq-wl.a.run.app/api -H "Content-Type: application/json" -d '{"project_id":"peerless-sensor-414405"}'
additional test case requried for the testing this with proper invocation as above invocation on the cloud shell will result in an error.
