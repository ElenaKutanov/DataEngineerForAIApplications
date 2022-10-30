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

![alt text](DependencyGraph.png)

- It's no need to divide frontend on services, because it is only one rote used and two components, which are connected the route.

- On the backend side I see three clear parts which can be divided on services (Locations, Persons and Connection).
We will start with the Location first, because it has logic that is much less tied to other parts of the API monolith.

- As I see, for the route "/locations" the code is missing. It should be fixed.

-----------------------------------------------------------------------------------------------
> vagrant up
> vagrant ssh
> sudo cat /etc/rancher/k3s/k3s.yaml
copy paste in C:\Users\elena\.kube\config
> exit
> kubectl describe services
> kubectl apply -f deployment/
> kubectl get pods
> sh scripts/run_db_command.sh <POD_NAME>

> docker rmi udaconnect-locations-api
> docker rmi elenakutanov/udaconnect-locations-api
> docker images

Image API changed:
> docker build -t udaconnect-api modules\api

> cd modules
> docker build -t udaconnect-locations-api -f locations_api/Dockerfile .

> docker images

NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes                 ClusterIP   10.43.0.1       <none>        443/TCP          132m
postgres                   NodePort    10.43.185.63    <none>        5432:32089/TCP   127m
udaconnect-api             NodePort    10.43.128.4     <none>        5000:30001/TCP   127m
udaconnect-app             NodePort    10.43.214.154   <none>        3000:30000/TCP   127m
udaconnect-locations-api   NodePort    10.43.82.169    <none>        5001:30002/TCP   97s

> docker image tag udaconnect-api:latest elenakutanov/udaconnect-api:latest
> docker push elenakutanov/udaconnect-api:latest

> docker image tag udaconnect-locations-api:latest elenakutanov/udaconnect-locations-api:latest
> docker push elenakutanov/udaconnect-locations-api:latest

> kubectl delete deployment udaconnect-locations-api
> kubectl delete services udaconnect-locations-api
> cd ..
> kubectl apply -f deployment/
> kubectl get pods


