# Getting started: Event API

To receive data from PortXchange, Event API can be used.

Event API provides a list of events we received in our system and assigned to a port call during
a provided timeframe (with an assignment time within that timeframe). Because of the amount of
events we receive daily, user is also expected to specify the port of interest, as otherwise the
size of the response could end up being too much to process.

**Note:** Most of the time the *assignment time* of an event coincides with the moment we
received that event in our system (i.e. *record time*). However, there are cases when an
event gets re-assigned to a different port call, ending up with a new *assignment time*. Using
*assignment time* for comparing against the provided timeframe ensures that the users receive
updates of event re-assignments.

Please note that the events you will receive are not necessarily all the events we have available in
our system, but the subset of events you are allowed to see based on our data authorization model.

**Attention!** 
Even after specifying the port, the response payload can still contain a large number of events. In that
case please adjust the requested timespan accordingly.

## Using Event API

Event API provides the user with 2 endpoints to use, `overview-events` and
`relevant-overview-events`. The first one returns all the events the user is allowed to see for the
provided query parameters. The second one provides only events relevant to the portcalls the user's
company has contributed events to.

To query data, you have to send a `GET` request to the URL (for 2nd endpoint just replace
`overview-events` with `relevant-overview-events` in the url): 
- for TEST environment: https://exchange.port-xchange.com/test/v1/api/overview-events
- for ACCEPTANCE environment: https://exchange.port-xchange.com/accp/v1/api/overview-events
- for PRODUCTION environment: https://exchange.port-xchange.com/prod/v1/api/overview-events

*Attention!* 
For each environment, you must create a separate set of credentials.

The URL contains next parameters:

- `from` - the start timestamp of the timeframe to fetch data. The parameter is **required**.
- `to` - the end timestamp of the timeframe. The parameter is **optional**. If not provided, the default value is current time.
- `port` - the UNLOCODE of the port to fetch data. The parameter is **required**.

Timestamp format is `YYYY-MM-ddTHH:mm:ssZ`.
For example, this is a valid value `2021-10-12T13:00:00Z`.

Response for the successful request (HTTP CODE 200) will contain a list of events.
~~The event format is described in [the format document](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts).~~

Unsuccessful requests can be next:
- Unauthorized (HTTP CODE 401) - the request does not provide correct API key
- Forbidden (HTTP CODE 403) - the request does not contain correct Company ID

Check the [example implementation](/resources/event_api.py) and [command line command](/resources/event_api.sh) for more details.

## Changelog

Important updates for the APIs will be published on the [Changelog](/sending-data/changelog.md) page.