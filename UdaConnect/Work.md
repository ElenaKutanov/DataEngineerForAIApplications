# Strategy

There are three services in initial app.
- database (postgres)
- bakend (udaconnect-api)
- frontend (udaconnect-app)

NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes       ClusterIP   10.43.0.1       <none>        443/TCP          12m
postgres         NodePort    10.43.210.191   <none>        5432:30850/TCP   84s
udaconnect-api   NodePort    10.43.192.216   <none>        5000:30001/TCP   84s
udaconnect-app   NodePort    10.43.27.184    <none>        3000:30000/TCP   84s

The dependancy graph:

![alt text](InitialDependencyGraph.png)

- It's no need to divide frontend on services, because it is only one rote used and two components, which are connected the route.

- On the backend side I see three clear parts which can be divided on services (Locations, Persons and Connection).
We will start with the Location first, because it has logic that is much less tied to other parts of the API monolith.

- As I see, for the route "/locations" the code is missing. It should be fixed.

- For intern exchange between connection and persons microservices, was choosed gRPC

-----------------------------------------------------------------------------------------------
> vagrant up
> vagrant ssh
> sudo cat /etc/rancher/k3s/k3s.yaml
copy paste in C:\Users\elena\.kube\config
> exit
> kubectl describe services
> kubectl apply -f deployment/
> kubectl get pods
> sh scripts/run_db_locations.sh <POD_NAME>
> sh scripts/run_db_persons.sh <POD_NAME>

> docker rmi udaconnect-app
> docker rmi elenakutanov/udaconnect-app

> docker rmi udaconnect-api-locations
> docker rmi elenakutanov/udaconnect-api-locations

> docker rmi udaconnect-api-persons
> docker rmi elenakutanov/udaconnect-api-persons

> docker rmi udaconnect-api-connection
> docker rmi elenakutanov/udaconnect-api-connection
> docker images

Image API changed:

> docker build -t udaconnect-app modules/frontend

> cd modules
> docker build -t udaconnect-api-locations -f api_locations/Dockerfile .
> docker build -t udaconnect-api-persons -f api_persons/Dockerfile .
> docker build -t udaconnect-api-connection -f api_connection/Dockerfile .

> docker images

REPOSITORY                               TAG       IMAGE ID       CREATED         SIZE
elenakutanov/udaconnect-app              latest    0d7dafa39ac9   5 minutes ago   551MB
udaconnect-app                           latest    0d7dafa39ac9   5 minutes ago   551MB
udaconnect-api-connection                latest    6272eb584bf5   21 hours ago    547MB
elenakutanov/udaconnect-api-connection   latest    6272eb584bf5   21 hours ago    547MB
elenakutanov/udaconnect-api-persons      latest    2dfcf333dc3d   21 hours ago    547MB
udaconnect-api-persons                   latest    2dfcf333dc3d   21 hours ago    547MB
elenakutanov/udaconnect-api-locations    latest    74b059ee834f   21 hours ago    547MB
udaconnect-api-locations                 latest    74b059ee834f   21 hours ago    547MB


> docker image tag udaconnect-app:latest elenakutanov/udaconnect-app:latest
> docker push elenakutanov/udaconnect-app:latest

> docker image tag udaconnect-api:latest elenakutanov/udaconnect-api:latest
> docker push elenakutanov/udaconnect-api:latest

> docker image tag udaconnect-api-locations:latest elenakutanov/udaconnect-api-locations:latest
> docker push elenakutanov/udaconnect-api-locations:latest

> docker image tag udaconnect-api-persons:latest elenakutanov/udaconnect-api-persons:latest
> docker push elenakutanov/udaconnect-api-persons:latest

> docker image tag udaconnect-api-connection:latest elenakutanov/udaconnect-api-connection:latest
> docker push elenakutanov/udaconnect-api-connection:latest


> kubectl delete deployment udaconnect-app
> kubectl delete services udaconnect-app

> kubectl delete deployment udaconnect-api-locations
> kubectl delete services udaconnect-api-locations

> kubectl delete deployment udaconnect-api-persons
> kubectl delete services udaconnect-api-personsc

> kubectl delete deployment udaconnect-api-connection
> kubectl delete services udaconnect-api-connection

> cd ..
> kubectl apply -f deployment/
> kubectl get pods


# gRPC

> python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ person.proto



# Check container
> kubectl exec --stdin --tty udaconnect-api-persons-866b867d46-4hstx -- /bin/sh
> kubectl exec --stdin -c udaconnect-persons-grpc-server --tty udaconnect-api-persons-866b867d46-4hstx -- /bin/sh
> kubectl exec --stdin -c udaconnect-locations-kafka-consumer --tty pod -- /bin/sh
> kubectl describe <POD_NAME>

# Check logs in all containers!
> kubectl logs -f deployment/udaconnect-api-locations --all-containers=true --since=10m
