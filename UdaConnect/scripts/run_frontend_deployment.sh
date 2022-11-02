# Erase images
docker rmi udaconnect-app
docker rmi elenakutanov/udaconnect-app

# Erase k8s services and deployments
kubectl delete deployment udaconnect-app
kubectl delete services udaconnect-app

# Build new images
docker build -t udaconnect-app modules/frontend

# Tag and push the images to DockerHub
docker image tag udaconnect-app:latest elenakutanov/udaconnect-app:latest
docker push elenakutanov/udaconnect-app:latest

# Apply deployments
kubectl apply -f deployment/

kubectl get pods