# docker_trial
Trial with creating lambda docker image

## How to use
1. clone repository to your local - `git clone <link>`
2. navigate to repo folder - `cd docker_trial`
3. build docker image - `docker build .`
4. find out the name of the image that is built `docker images`
5. run the image `docker run -p 9000:8080 <first three characters of the image name>`

Steps 1 to 5 will create an lambda function api end point that is running in port 8080 of your system. Then open another termina to make calls to the lambda api

6. `script.sh` has a sample script to make calls to the lambda api. Run `sh script.sh`

This should give you a response like this

```
{"statusCode": 200, "body": {"Hi there": "Hello"}}
```
