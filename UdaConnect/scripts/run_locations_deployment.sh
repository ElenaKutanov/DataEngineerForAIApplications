# Erase images
docker rmi udaconnect-api-locations
docker rmi elenakutanov/udaconnect-api-locations
docker rmi udaconnect-api-locations-kafka
docker rmi elenakutanov/udaconnect-api-locations-kafka

# Erase k8s services and deployments
kubectl delete deployment udaconnect-api-locations
kubectl delete services udaconnect-api-locations

# Build new images
# Moved to get access to parent folder
cd modules/api_locations/
docker-compose build
cd ../..

# Tag and push the images to DockerHub
docker image tag udaconnect-api-locations:latest elenakutanov/udaconnect-api-locations:latest
docker push elenakutanov/udaconnect-api-locations:latest

docker image tag udaconnect-api-locations-kafka:latest elenakutanov/udaconnect-api-locations-kafka:latest
docker push elenakutanov/udaconnect-api-locations-kafka:latest