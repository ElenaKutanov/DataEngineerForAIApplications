# Erase images
docker rmi udaconnect-kafka-producer
docker rmi elenakutanov/udaconnect-kafka-producer
docker rmi udaconnect-kafka-broker
docker rmi elenakutanov/udaconnect-kafka-broker

# Erase k8s services and deployments
kubectl delete deployment udaconnect-kafka-producer
kubectl delete services udaconnect-kafka-producer

kubectl delete deployment udaconnect-kafka-broker
kubectl delete services udaconnect-kafka-broker

# Build new image
docker build -t udaconnect-kafka-broker modules/kafka_broker
docker build -t udaconnect-kafka-producer modules/kafka_producer

# Tag and push the images to DockerHub
docker image tag udaconnect-kafka-broker:latest elenakutanov/udaconnect-kafka-broker:latest
docker push elenakutanov/udaconnect-kafka-broker:latest

docker image tag udaconnect-kafka-producer:latest elenakutanov/udaconnect-kafka-producer:latest
docker push elenakutanov/udaconnect-kafka-producer:latest