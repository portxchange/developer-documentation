#!/usr/env/sh

curl --location --request GET 'https://api.developer-portal.port-xchange.com/prod/v1/share/pull?from=2021-10-12T13%3A00%3A00Z&to=2021-10-12T17%3A00%3A00Z' \
  --header 'Content-Type: application/json' \ 
  --header 'Accepts: application/json' \
  --header 'X-Company-Id: $YOUR_COMPANY_ID' \
  --header 'X-Api-Key: $YOUR_API_KEY'