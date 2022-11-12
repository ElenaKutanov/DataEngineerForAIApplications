# Erase images
docker rmi udaconnect-api-persons
docker rmi elenakutanov/udaconnect-api-persons
docker rmi udaconnect-api-persons-grpc
docker rmi elenakutanov/udaconnect-api-persons-grpc


# Erase k8s services and deployments
kubectl delete deployment udaconnect-api-persons
kubectl delete services udaconnect-api-persons

# Build new images
# Moved to get access to parent folder
cd modules/api_persons
docker-compose build
cd ../..


# Tag and push the images to DockerHub
docker image tag udaconnect-api-persons:latest elenakutanov/udaconnect-api-persons:latest
docker push elenakutanov/udaconnect-api-persons:latest

docker image tag udaconnect-api-persons-grpc:latest elenakutanov/udaconnect-api-persons-grpc:latest
docker push elenakutanov/udaconnect-api-persons-grpc:latest