# Dockerized Python App

## Preparation

- It's nice to have docker installed.
- Check if `./app.sh` is executable.
- Available operations:
  1. `build` build the container;
  2. `stop` stop the container;
  3. `status` show the status of the container.
- You can check the endpoints below.

```
Example:
   ./app.sh build
   ./app.sh status
```

## Available endpoints

- You can use the IP Address from the slave container or the IP Address from the application container (flask_app) inside the slave container
- <http://0.0.0.0:8280/> : returns Hello World!
- <http://0.0.0.0:8280/pwd> : returns Where you are
- <http://0.0.0.0:8280/healthchecker> : return an OK
- <http://0.0.0.0:8280/conf/env> : returns Linux environment variables using env
- <http://0.0.0.0:8280/conf/printenv> : returns Linux environment variables using printenv
- <http://0.0.0.0:8280/env/{env_name}/{env_v}> : create a new Linux environment variable with `env_name` and `env_v` parameters that you need to provide
  - If you want to test it use env or printenv endpoints
- <http://0.0.0.0:8280/running-software> : returns all processes that is running
- <http://0.0.0.0:8280/running-software/{serv_name}>: returns the process specified by `serv_name` that you need to provide
