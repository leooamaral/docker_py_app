#!/bin/bash

help(){
    echo "Syntax: ./app.sh [-h] or [[start|status|stop] ]"
    echo
    echo "Options:"
    echo "-h        Print the help"
    echo
    echo "Operations:"
    echo "start     Build and start container"
    echo "stop      Stop container"
    echo "status    Show the status of the container"
    
}


start_docker(){
    if [[ "$(docker ps -a -f name=flask_app -q)" ]]; then
        echo "Starting the exited service"
        docker start "$(docker ps -a -f name=flask_app -q)"        
    elif [[ "$(docker images -q flask_app)" ]]; then 
        echo "Running the service that already was build"
        docker run -d --rm -p 8080:8080 --name flask_app flask_app   
    else
        echo "Building service and running"
        docker build -t flask_app .
        docker run -d --rm -p 8080:8080 --name flask_app flask_app        
    fi
}


status_docker(){
    echo "Choose option 1 to see the status of the container created"
    echo "Choose option 2 to see all running containers or exited services"
    read option

    if [[ option -eq 1 ]]; then
        if [[ "$(docker ps -aq -f status=running -f name=flask_app)" ]]; then
            echo "Container is running!!"
        else
            echo "Container is not running!!"
        fi
    else
        echo "Showing all running services or exited services"
        docker ps -a
    fi
}


stop_docker(){
    if [[ "$(docker ps -a -f name=flask_app -q)" ]]; then
        echo "Stopping container"
        docker stop flask_app        
    else
        echo "Container is not up"
    fi
}

while getopts ":h" option; do
   case $option in
      h) # display Help
         help
         exit;;
   esac
done

case "$1" in
    start)
        start_docker
        ;;
    status)
        status_docker
        ;;
    stop)
        stop_docker
        ;;
        
    *)
        echo "Option doesn't exist"
        ;;
esac