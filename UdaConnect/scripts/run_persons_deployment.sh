# Erase images
docker rmi udaconnect-persons-api
docker rmi elenakutanov/udaconnect-persons-api


# Erase k8s services and deployments
kubectl delete deployment udaconnect-persons-api
kubectl delete services udaconnect-persons-api

# Build new images
# Moved to get access to parent folder
cd modules
docker build -t udaconnect-persons-api -f persons_api/Dockerfile .
cd ..

# Tag and push the images to DockerHub
docker image tag udaconnect-persons-api:latest elenakutanov/udaconnect-persons-api:latest
docker push elenakutanov/udaconnect-persons-api:latest