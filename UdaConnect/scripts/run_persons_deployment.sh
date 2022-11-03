# Erase images
docker rmi udaconnect-api-persons
docker rmi elenakutanov/udaconnect-api-persons


# Erase k8s services and deployments
kubectl delete deployment udaconnect-api-persons
kubectl delete services udaconnect-api-persons

# Build new images
# Moved to get access to parent folder
cd modules
docker build -t udaconnect-api-persons -f api_persons/Dockerfile .
cd ..

# Tag and push the images to DockerHub
docker image tag udaconnect-api-persons:latest elenakutanov/udaconnect-api-persons:latest
docker push elenakutanov/udaconnect-api-persons:latest