import os
from pprint import pprint
import requests

# The examples get the current visit details for the ship with imo 9795625
#
# The example uses TEST environemnt.
# Full list of URLS:
# - TEST: https://exchange.port-xchange.com/test/
# - ACCP: https://exchange.port-xchange.com/accp/
# - PROD: https://exchange.port-xchange.com/prod/
#
#
# Run the example with `python ship_api.py` command
# Ensure that you provide correct `COMPANY_ID` and `API_KEY` environment variables


def main():
  # Source, Comapny ID and API key are provided
  # Check Developer Portal to get corresponding values
  company_id = os.environ['COMPANY_ID']
  api_key = os.environ['API_KEY']

  headers = {
    # The API talks in JSON
    'Content-Type': 'application/json',
    'Accepts': 'application/json',
    # Authorization
    'X-Company-Id': company_id,
    'X-Api-Key': api_key,
  }

  url = 'https://exchange.port-xchange.com/test/v1/api/ships/9795625/visits/current'
  result = requests.get(url, headers = headers)

  pprint(result.status_code)
  pprint(result.json())

if __name__ == '__main__':
  main()