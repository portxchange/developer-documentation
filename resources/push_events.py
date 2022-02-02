from datetime import datetime, timedelta
import os
from pprint import pprint 
import requests
import uuid

# TODO: verify URLs and links to the docs
# The examples submits 2 events to the PortXchange API:
# - estimate arrival to berth
# - estimate departure from berth
#
# For the format specification see: https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts
#
# The example uses TEST environemnt.
# Full list of URLS:
# - TEST: https://exchange.port-xchange.com/test/
# - ACCP: https://exchange.port-xchange.com/accp/
# - PROD: https://exchange.port-xchange.com/prod/
#
#
# Run the example with `python push_events.py` command
# Ensure that you provide correct `COMPANY_ID`, `API_KEY`, and `SOURCE` environment variables


# The API accepts dates in YYYY-MM-DDThh:mm:ssTZD format
# Example "2017-09-01T12:00:12Z"
# this code strips millis from the timestamp and adds 'Z' letter
# because the author is lazy enough to get into Python date-time formats
def iso_date_str(date):
  return date.isoformat()[:-7] + 'Z'


# Prepare the events
def get_events(source): 
  record_time = iso_date_str(datetime.utcnow())
  arrival_time = iso_date_str(datetime.utcnow() + timedelta(hours=2))
  departure_time = iso_date_str(datetime.utcnow() + timedelta(hours=12))
  berth_visit_id = str(uuid.uuid1())
  # Organization portcall id must start with 'PID-'
  org_portcall_id = 'PID-' + str(uuid.uuid1())

  eta = {
    'uuid': str(uuid.uuid1()),
    # Source is provided with API credentials
    'source': source,
    # Consult with https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L215
    'eventType': 'berth.eta.terminal',
    'recordTime': record_time,
    'eventTime': arrival_time,
    # Port UNLOCODE
    'port': 'USHOU',
    'location': {
      # Consult with https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L343
      'type': 'berth',
      'name': 'LBC Barge 1',
    },
    'context': {
      'organisationPortcallId': org_portcall_id,
      'berthVisitId': berth_visit_id,
    },
    'ship': {
      # Provide one of the identifiers IMO/MMSI/USCG/ENI
      # name field is informative only
      "imo":"9177521",
      "mmsi":"413236310",
      "name":"SHANG HANG 98"
    }
  }
  etd = {
    'uuid': str(uuid.uuid1()),
    'source': source,
    'eventType': 'berth.etd.terminal',
    'recordTime': record_time,
    'eventTime': departure_time,
    'port': 'USHOU',
    'location': {
      'type': 'berth',
      'name': 'LBC Barge 1',
    },
    'context': {
      'organisationPortcallId': org_portcall_id,
      'berthVisitId': berth_visit_id,
    },
    'ship': {
      "imo":"9177521",
      "mmsi":"413236310",
      "name":"SHANG HANG 98"
    }
  }

  return [eta, etd]


def main():
  # Source, Comapny ID and API key are provided
  # Check Developer Portal to get corresponding values
  company_id = os.environ['COMPANY_ID']
  api_key = os.environ['API_KEY']
  source = os.environ['SOURCE']

  headers = {
    # The API talks in JSON
    'Content-Type': 'application/json',
    'Accepts': 'application/json',
    # Authorization
    'X-Company-Id': company_id,
    'X-Api-Key': api_key,
  }

  for event in get_events(source):
    # submit the event 
    submit_req = requests.post('https://exchange.port-xchange.com/test/v1/api/event', json = event, headers = headers)
    pprint(submit_req.status_code)
    pprint(submit_req.json())


if __name__ == '__main__':
  main()
