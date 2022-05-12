# docker_trial
Trial with creating lambda docker image

## How to use
1. clone repository to your local - `git clone <link>`
2. navigate to repo folder - `cd docker_trial`
3. build docker image - `docker build . -t docker_trial`
4. run the image `docker run -p 9000:8080 --rm docker_trial`

Steps 1 to 4 will create an lambda function api end point that is running in port 8080 of your system. Then open another termina to make calls to the lambda api

5. `script.sh` has a sample script to make calls to the lambda api. Run `sh script.sh`

This should give you a response like this

```
{"statusCode": 200, "body": {"Hi there": "Hello"}}
```

## To make changes to code and rebuild image

1. Remove existing image before rebuilding to avoid polluting your local maching with unused images `docker rmi docker_trial`
2. Make changes to your code and start from step 2 above
