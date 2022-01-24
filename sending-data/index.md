# Getting started: Sending Data

Push API is used to push events into the Port-Xchange data pool. Once pushed the event will be processed into a port call.

The events must be submitted one at a time.

The events must be unique and have unique UUID. However, the same payload can be sumbitted multiple times.

To update data of the event, the changed payload must be submitted and it must have new, unique UUID. 

If the event property has to be removed, it is possible to sumbit `null`-data as a property value. For example, if the location that was submitted before becomes invalid and unknown, the update payload can contain `"location": null` value.

The API requires authorization, for more information consult with the [Authorization](/authorization.md) page.

## Using Push API

Push API can be used to submit events one at a time.

To query data, you have to send a `POST` request to the URL: // TODO: provide a URL

The API accepts JSON-encoded objects of the format described below.

Response for the successful request will contain the accepted event payload (HTTP CODE 200).

Unsuccessful requests can be next:
- Bad Request (HTTP CODE 400) - the payload is malformed or contains conflicting data. The explanation is provided in the response payload.
- Unauthorized (HTTP CODE 401) - the request does not provide correct API key
- Forbidden (HTTP CODE 403) - the request does not contain correct Comapny ID

Check the [example implementation](/resources/push_event.py) and [command line command](/resources/push_event.sh)  for more details.

## Event format

The port call event format is an implementation of the funtional definitions for Nautical Port Information Standard (NPIS) 5.2.

The event format is fully described in [the format document](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts).

Every event must be JSON-encoded and contain next fields:
- eventTime - a timestamp when the event is happening;
- eventType - a type of the event. Full list of the events can be found in the [specification](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L214-L416);
- port - a UNLOCODE of a port, where the event is happening;
- recordTime - a timestamp when the event is registered or issued, the timestamp cannot be in future;
- ship - an object containing one of the supported identifiers: `IMO`, `MMSI`, `ENI`, `USCG`
- source - a name of the system or organization that provides the event;
- uuid - a unique identifier of the event ([what is uuid](https://www.uuidtools.com/what-is-uuid));
- version - a version.

**Attention!** 
A vessel name provided in the `ship` object will not be used as a vessel identifier.

### MovementId, BerthVisitId, ServiceId and OrganisationPortcallId

The event system allows for three additional identifiers in addition to portcall id's:
* Movement identifier: this identifies a movement, which is a ship traveling from one location to another inside a portcall
* Berth visit identifier: this identifies a berth visit, which is a ship being alongside a single berth
* Service identifier: this identifies a single service like bunkering
* Organisation port call identifier: this identifies a visit, which is a ship its stay within a single port. This is an internal identifier for an organization, independant of the port call id which is the identifier of the local port authority.

| ID                                | Format              |
|-----------------------------------|---------------------|
| Movement identifier               | `MID-{SYSTEM}-{ID}` |
| Berth visit identifier            | `BID-{SYSTEM}-{ID}` |
| Service identifier                | `SID-{SYSTEM}-{ID}` |
| Organisation port call identifier | `PID-{SYSTEM}-{ID}` |

`{SYSTEM}` must be replaced by a string consisting of alphanumeric characters or an underscore (`[A-Z0-9_]`) of which can reasonably be assumed that it globally uniquely identifies the system sending events.

`{ID}` must be replaced by a string consisting of of alphanumeric characters or an underscore (`[A-Z0-9_]`) which is unique for that system.

## Restrictions

- An event MUST NOT contain both a movement and berth visit identifier.
- A system MUST NOT use both movement and berth visit identifiers, it can only send one type in its events.
- A system SHOULD prefer movement identifiers over berth visit identifiers, unless it only sends events about berth activities.
- An event belonging to a berth visit activity with a movement identifier MUST be interpreted as belonging to the berth visit following that movement
- A system MUST use the same identifier if it sends new events about the same activity, unless that identifier was cancelled in case it MUST create a new one.
- A system MUST NOT re-use identifiers.
- A system MAY omit a movement or berthvisit identifier if a portcall only has a single berthvisit and two movements (an inbound and outbound movement)
_ A system SHOULD NOT send new events with an identifier it previously cancelled, since those events will be considered part of the now cancelled activity.
- A system MAY omit berth visit and movement identifiers for actual events.

## Locations 

The event payload has `location` field. The field is usually represented by location type, e.g. "terminal" or "pilotBoardingPlace", and a name.

An integrating system can provide location names in a format that is used internally.
Port-Xchange system uses internal procedures to match identifiers provided by an external system with internal location identifiers.

The full list of event location types can be found in the [specification](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L419-L428).

**Attention!** 
If you would like to use simple identifiers of locations, for example, numbers, contact the Port-Xchange support in advance. 

## Use Cases

We describe more specific use-cases on the following pages:

- [Integrating with Push API as a Port Authority](/sending-data/use-case-port-authority.md)
- [Integrating with Push API as an Agent](/sending-data/use-case-agent.md)
- [Integrating with Push API as a Terminal](/sending-data/use-case-terminal.md)
- [Integrating with Push API as a Carrier](/sending-data/use-case-carrier.md)
- [Integrating with Push API as a Service Provider](/sending-data/use-case-service-provider.md)

## Changelog

Important updates for the APIs will be published on the [Changelog](/sending-data/changelog.md) page.