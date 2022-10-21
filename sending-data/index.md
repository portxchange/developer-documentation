# Getting started: Sending Data

Exchange API can be used to send events into the PortXchange data pool. Once pushed, the event will
be processed into a port call.

The events must be submitted one at a time.

The events must be unique and have unique UUID. However, the same payload can be sumbitted multiple
times.

To update data of the event, the changed payload must be submitted and it must have new, unique UUID. 

If the event property has to be removed, it is possible to sumbit `null`-data as a property value.
For example, if the location that was submitted before becomes invalid and unknown, the update
payload can contain `"location": null` value.

To use the Exchange API for sending events, please consult the [Exchange API Docs](https://portxchange.github.io/exchange-api-docs/).
For examples of sending an event via Exchange API, refer to [Python implementation example](/resources/push_event.py)
and [command line example](/resources/push_event.sh). Keep in mind that all endpoints require the API
key and company ID headers, as described in [Authorization](/authorization.md) page.

## Event format

The port call event format is an implementation of the functional definitions for Nautical Port Information Standard (NPIS) 5.2.

The event format is fully described in the [Exchange API Docs](https://portxchange.github.io/exchange-api-docs/#/routes/post-event).

Every event must be JSON-encoded and contain next fields:
- eventTime - a timestamp when the event is happening;
- eventType - a type of the event. Full list of the events can be found in the API docs.
- port - a UNLOCODE of a port, where the event is happening;
- recordTime - a timestamp when the event is registered or issued, the timestamp cannot be in future; if no
  recordTime is provided, the timestamp of the moment the event reaches PortXchange is used
- ship - an object containing one of the supported identifiers: `IMO`, `MMSI`, `ENI`, `USCG`
- uuid - a unique identifier of the event ([what is uuid](https://www.uuidtools.com/what-is-uuid));
  if no uuid is provided, a random one is assigned to the event

**Attention!** 
A vessel name provided in the `ship` object will not be used as a vessel identifier.

### MovementId, BerthVisitId, ServiceId and OrganisationPortcallId

The event system allows for four additional identifiers in addition to `localPortcallId`:
* Movement identifier: this identifies a movement, which is a ship traveling from one location to another inside a portcall
* Berth visit identifier: this identifies a berth visit, which is a ship being alongside a single berth
* Service identifier: this identifies a single service like bunkering
* Organisation port call identifier: this identifies a visit, which is a ship its stay within a single port. This is an internal identifier for an organization, independent of the `localPortcallId` which is the identifier of the local port authority.

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
- A system SHOULD prefer movement identifiers over berth visit identifiers unless it only sends events about berth activities. It is suggested that agents, carriers, and port authorities submit movement identifiers, and terminals submit berth visit identifiers. Service providers should prefer service identifiers.
- A system MUST use the same identifier if it sends new events about the same activity, unless that identifier was cancelled in case it MUST create a new one.
- A system MUST NOT re-use identifiers.
- A system MAY omit a movement or berthvisit identifier if a portcall only has a single berthvisit and two movements (an inbound and outbound movement)
_ A system SHOULD NOT send new events with an identifier it previously cancelled, since those events will be considered part of the now cancelled activity.
- A system MAY omit berth visit, movement, and service identifiers for actual events.

## Locations 

The event payload has `location` field. The field is usually represented by location type, e.g. "terminal" or "pilotBoardingPlace", and a name.

An integrating system can provide location names in a format that is used internally.
PortXchange system uses internal procedures to match identifiers provided by an external system with internal location identifiers.

The full list of event location types can again be found in the API docs.

**Attention!** 
If you would like to use simple identifiers of locations, for example, numbers, contact the PortXchange support in advance. 

## Use Cases

We describe more specific use-cases on the following pages:

- [Integrating with Push API as a Port Authority](/sending-data/use-case-port-authority.md)
- [Integrating with Push API as an Agent](/sending-data/use-case-agent.md)
- [Integrating with Push API as a Terminal](/sending-data/use-case-terminal.md)
- [Integrating with Push API as a Carrier](/sending-data/use-case-carrier.md)
- [Integrating with Push API as a Service Provider](/sending-data/use-case-service-provider.md)
