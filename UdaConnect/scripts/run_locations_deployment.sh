# Erase images
docker rmi udaconnect-api-locations
docker rmi elenakutanov/udaconnect-api-locations
docker rmi udaconnect-api-locations-kafka
docker rmi elenakutanov/udaconnect-api-locations-kafka
docker rmi udaconnect-kafka-broker
docker rmi elenakutanov/udaconnect-kafka-broker

# Erase k8s services and deployments
kubectl delete deployment udaconnect-api-locations
kubectl delete services udaconnect-api-locations

kubectl delete deployment udaconnect-kafka-broker
kubectl delete services udaconnect-kafka-broker

# Build new images
# Moved to get access to parent folder
cd modules/api_locations/
docker-compose build
cd ../..
docker build -t udaconnect-kafka-broker modules/kafka_broker/

# Tag and push the images to DockerHub
docker image tag udaconnect-api-locations:latest elenakutanov/udaconnect-api-locations:latest
docker push elenakutanov/udaconnect-api-locations:latest

docker image tag udaconnect-api-locations-kafka:latest elenakutanov/udaconnect-api-locations-kafka:latest
docker push elenakutanov/udaconnect-api-locations-kafka:latest

docker image tag udaconnect-kafka-broker:latest elenakutanov/udaconnect-kafka-broker:latest
docker push elenakutanov/udaconnect-kafka-broker:latest