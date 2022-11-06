# Erase images
docker rmi udaconnect-api-connection
docker rmi elenakutanov/udaconnect-api-connection

# Erase k8s services and deployments
kubectl delete deployment udaconnect-api-connection
kubectl delete services udaconnect-api-connection

# Build new images
docker build -t udaconnect-api-connection modules/api_connection/

# Tag and push the images to DockerHub
docker image tag udaconnect-api-connection:latest elenakutanov/udaconnect-api-connection:latest
docker push elenakutanov/udaconnect-api-connection:latest