#!/bin/bash

# Generate private key + self-signed certificate in separate files
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key

