# Fast API Model Serving with Iris Dataset Use Case

### How to Run

#### Development setup

1. create virtual env: `python3 -m venv venv`
2. install all deps: `poetry install`
3. run service: `pre-commit install`

#### Local

1. create virtual env: `python3 -m venv venv`
2. install all deps: `poetry install`
3. run service: `task app`
4. swagger API docs can be accessed at `http://0.0.0.0:8001/docs` in your chrome browser

#### Docker

1. Make sure you have docker in your local computer

2. Build docker image

   ```
   docker build -t iris-api:v1.0.0 .
   ```

   This command will create the docker image with the name iris-api and tag `v1.0.0`
   `-t` is the flag to give tag of the docker image.

3. Run docker image as container
   ```
   docker run -d --name iris-api-container -p 8001:8001 iris-api:v1.0.0
   ```
   This command will run the docker container with our named image `iris-api` that have `v1.0.0-rc1` version.
   The running container will run as container with name `iris-api-container` and running on port `1234`.
   The running container will run on detach mode (means our terminal didn't attached directly with the docker container)
   -d is the flag to indicate the container should run in detach mode
   --name is the flag to named the container
   -p will map the container port in `8001` to host port in `1234`. Therefore, our app accessible in `http://127.0.0.1:1234`. The swagger are accessible at `http://127.0.0.1:1234/docs`
