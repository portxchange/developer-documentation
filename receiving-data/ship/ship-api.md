# Getting started: Ship API

To retrieve the current or upcoming visit of a ship from PortXchange, the Ship API can be used.

The Ship API provides the current visit details of the provided ship (if exists) with the ship's metadata.

## Using Ship API

To query data, you have to send a `GET` request to the URL:

- for TEST environment: https://exchange.port-xchange.com/test/v1/api/ships/{{ship_id}}/visits/current
- for ACCEPTANCE environment: https://exchange.port-xchange.com/accp/v1/api/ships/{{ship_id}}/visits/current
- for PRODUCTION environment: https://exchange.port-xchange.com/prod/v1/api/ships/{{ship_id}}/visits/current

*Attention!*
For each environment, you must create a separate set of credentials.

The URL contains :

- `ship_id` - the imo or mmsi of the ship for which the current visit details are requested **required**.
- `port` - the optional port query parameter. If provided it returns the current or upcoming visit for the given ship and port. 

Response for the successful request (HTTP CODE 200) will contain the ship metadata and visit details if the visit is found. 
The example for the success response is provided in [example](/resources/ship_success_response.json).

If visit for the ship for the particular ship is not found then response will be (HTTP CODE 200) with message. The
example for the response is provided in [example](/resources/ship_visit_not_found_response.json).

Unsuccessful requests can be next:

- Unauthorized (HTTP CODE 401) - the request does not provide correct API key
- Forbidden (HTTP CODE 403) - the request does not contain correct Company ID

Check the [example implementation](/resources/ship_api.py) and [command line command](/resources/ship_api.sh) for more
details.

## Changelog

Important updates for the APIs will be published on the [Changelog](/receiving-data/ship/changelog.md) page.