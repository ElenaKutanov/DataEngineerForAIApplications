# Erase images
docker rmi udaconnect-kafka
docker rmi elenakutanov/udaconnect-kafka

# Erase k8s services and deployments
kubectl delete deployment udaconnect-kafka
kubectl delete services udaconnect-kafka

# Build new image
cd modules/kafka
docker-compose up -d
cd ../..

# Tag and push the images to DockerHub
docker image tag udaconnect-kafka:latest elenakutanov/udaconnect-kafka:latest
docker push elenakutanov/udaconnect-kafka:latest