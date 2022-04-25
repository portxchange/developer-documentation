#!/usr/env/sh

curl --location --request GET 'https://exchange.port-xchange.com/test/v1/api/ships/9795625/visits/current' \
  --header 'Content-Type: application/json' \
  --header 'Accepts: application/json' \
  --header 'X-Company-Id: $YOUR_COMPANY_ID' \
  --header 'X-Api-Key: $YOUR_API_KEY'