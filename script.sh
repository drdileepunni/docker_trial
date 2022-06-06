#!/usr/bin/env bash

INPUTDATA=`cat lambda_trial.json`
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "$INPUTDATA"
