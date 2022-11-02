# Erase images
docker rmi udaconnect-locations-api
docker rmi elenakutanov/udaconnect-locations-api

# Erase k8s services and deployments
kubectl delete deployment udaconnect-locations-api
kubectl delete services udaconnect-locations-api

# Build new images
# Moved to get access to parent folder
cd modules
docker build -t udaconnect-locations-api -f locations_api/Dockerfile .
cd ..

# Tag and push the images to DockerHub
docker image tag udaconnect-locations-api:latest elenakutanov/udaconnect-locations-api:latest
docker push elenakutanov/udaconnect-locations-api:latest

# Apply deployments
kubectl apply -f deployment/

kubectl get pods