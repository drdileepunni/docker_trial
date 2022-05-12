#!/usr/bin/env bash

INPUTDATA='{"My trial string":"trial"}'
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "$INPUTDATA"
