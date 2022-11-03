# Erase images
docker rmi udaconnect-api-connection
docker rmi elenakutanov/udaconnect-api-connection

# Erase k8s services and deployments
kubectl delete deployment udaconnect-api-connection
kubectl delete services udaconnect-api-connection

# Build new images
# Moved to get access to parent folder
cd modules
docker build -t udaconnect-api-connection -f api_connection/Dockerfile .
cd ..

# Tag and push the images to DockerHub
docker image tag udaconnect-api-connection:latest elenakutanov/udaconnect-api-connection:latest
docker push elenakutanov/udaconnect-api-connection:latest