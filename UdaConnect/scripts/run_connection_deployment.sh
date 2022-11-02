# Erase images
docker rmi udaconnect-connection-api
docker rmi elenakutanov/udaconnect-connection-api

# Erase k8s services and deployments
kubectl delete deployment udaconnect-connection-api
kubectl delete services udaconnect-connection-api

# Build new images
# Moved to get access to parent folder
cd modules
docker build -t udaconnect-connection-api -f connection_api/Dockerfile .
cd ..

# Tag and push the images to DockerHub
docker image tag udaconnect-connection-api:latest elenakutanov/udaconnect-connection-api:latest
docker push elenakutanov/udaconnect-connection-api:latest