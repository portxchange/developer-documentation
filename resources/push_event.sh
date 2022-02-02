#!/usr/env/sh

curl --location --request POST 'https://exchange.port-xchange.com/test/v1/api/event' \
  --header 'Content-Type: application/json' \ 
  --header 'Accepts: application/json' \
  --header 'X-Company-Id: $YOUR_COMPANY_ID' \
  --header 'X-Api-Key: $YOUR_API_KEY'
  --d '{"context": {"berthVisitId": "b9b2a082-7ac6-11ec-9798-acde48001122", "organisationPortcallId": "PID-b9b2a140-7ac6-11ec-9798-acde48001122"}, "eventTime": "2022-01-21T16:30:47Z", "eventType": "berth.eta.terminal", "location": {"name": "LBC Barge 1", "type": "berth"}, "port": "USHOU", "recordTime": "2022-01-21T14:30:47Z", "ship": {"imo": "9177521", "mmsi": "413236310", "name": "SHANG HANG 98"}, "source": "EXTERNAL_SYSTEM", "uuid": "b9b2a17c-7ac6-11ec-9798-acde48001122"}'