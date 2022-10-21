from datetime import datetime, timedelta
import os
from pprint import pprint 
import requests

# The examples queries events for the port calls finished between 4 and 2 hours ago
#
# The example uses TEST environemnt.
# Full list of URLS:
# - TEST: https://exchange.port-xchange.com/test/
# - ACCP: https://exchange.port-xchange.com/accp/
# - PROD: https://exchange.port-xchange.com/prod/
#
#
# Run the example with `python push_events.py` command
# Ensure that you provide correct `COMPANY_ID` and `API_KEY` environment variables

# The API accepts dates in YYYY-MM-DDThh:mm:ssTZD format
# Example "2017-09-01T12:00:12Z"
# this code strips millis from the timestamp and adds 'Z' letter
# because the author is lazy enough to get into Python date-time formats
def iso_date_str(date):
  return date.isoformat()[:-7] + 'Z'


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

  from_timestamp = iso_date_str(datetime.utcnow() - timedelta(hours=2))
  to_timestamp = iso_date_str(datetime.utcnow() - timedelta(hours=4))
  port = 'NLRTM'
  url = 'https://exchange.port-xchange.com/test/v1/api/events?from=%s&to=%s&port=%s' % (from_timestamp, to_timestamp, port)
  result = requests.get(url, headers = headers)

  pprint(result.status_code)
  pprint(result.json())

if __name__ == '__main__':
  main()