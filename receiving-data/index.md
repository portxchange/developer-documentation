# Getting started: Receiving data

To receive data from Port-Xchange, Event API can be used.

Event API provides a list of events forming the finished port calls in selected timeframe.

If the user requests events from midnight of the date A to midnight of the date B, the user will receive all events of port calls that finished at this period.

Finished port call is a port call with an actual time of departure from a port.

**Attention!** 
The response payload can contain a large number of events. Adjust the requested timespan if you receive more data than you can process.

## Using Event API

Event API can be used to fetch all events of a finished port call. 

To query data, you have to send a `GET` request to the URL: // TODO: URL

The URL contains next parameters:

- `from` - the start timestamp of the timeframe to fetch data. The prarameter is **required**.
- `to` - the end timestamp of the timeframe. The prarameter is **optional**. If not provided, the default value is current time.

Timestamp format is `YYYY-MM-ddTHH:mm:ssZ`.
For example, this is a valid value `2021-10-12T13:00:00Z`.

Response for the successful request (HTTP CODE 200) will contain a list of events. The event format is described in [the format document](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts).

Unsuccessful requests can be next:
- Unauthorized (HTTP CODE 401) - the request does not provide correct API key
- Forbidden (HTTP CODE 403) - the request does not contain correct Comapny ID

Check the [example implementation](/resources/event_api.py) and [command line command](/resources/event_api.sh) for more details.

## Limitations

1. Only deep-sea vessel port calls are supported.

## Changelog

Important updates for the APIs will be published on the [Changelog](/sending-data/changelog.md) page.