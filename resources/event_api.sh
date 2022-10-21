#!/usr/env/sh

curl --location --request GET 'https://exchange.port-xchange.com/test/v1/api/events?from=2021-10-12T13%3A00%3A00Z&to=2021-10-12T17%3A00%3A00Z&port=NLRTM' \
  --header 'Content-Type: application/json' \ 
  --header 'Accepts: application/json' \
  --header 'X-Company-Id: $YOUR_COMPANY_ID' \
  --header 'X-Api-Key: $YOUR_API_KEY'