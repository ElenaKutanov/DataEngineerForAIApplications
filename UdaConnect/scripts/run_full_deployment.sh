sh scripts/run_connection_deployment.sh
sh scripts/run_persons_deployment.sh
sh scripts/run_frontend_deployment.sh
sh scripts/run_locations_deployment.sh

# Erase db k8s services and deployments
kubectl delete deployment postgres-persons
kubectl delete services postgres-persons

kubectl delete deployment postgres-locations
kubectl delete services postgres-locations

# Apply deployments
kubectl apply -f deployment/

kubectl get pods