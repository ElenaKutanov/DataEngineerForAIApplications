# Erase images
docker rmi udaconnect-api-locations
docker rmi elenakutanov/udaconnect-api-locations

# Erase k8s services and deployments
kubectl delete deployment udaconnect-api-locations
kubectl delete services udaconnect-api-locations

# Build new images
docker build -t udaconnect-api-locations modules/api_locations/

# Tag and push the images to DockerHub
docker image tag udaconnect-api-locations:latest elenakutanov/udaconnect-api-locations:latest
docker push elenakutanov/udaconnect-api-locations:latest