we installed docker then minikube then loaded again which created self a docker container to run in as cannot run a server environment 
minikube start          // start the cluster (stop stops it..)
minikube dashboard      //this launched the webserver

after the started minikube installed in a container we can apply some deployment or config files using

kubctl apply -f <file>.yml


minikube status     //can show if all internal parts are up

 kubectl get pods   // shows pods
 kubectl get services   // shows existing services with confirguration


 minikube service <servicename>     //creates a tunnel to reach the app/service locally 127.0.0.1. need to remain open in cmd

 kubctl scale deployment <service> --replicas=9     //force to change how many replicas are to be used for