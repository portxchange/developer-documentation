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

### LocalPortcallId, OrganizationPortcallId, MovementId, BerthVisitId, LocationVisitId and ServiceId

The event system allows six different identifiers to be included in its context:
* `localPortcallId`: this identifies the port call, which is a ship's stay within a single port.
  It is the identifier used by the local port authority, recognised by other organizations.
* `organizationPortcallId`: this also identifies the port call, but it is the identifier used internally 
  by a single organization, e.g. terminal company. The main difference to `localPortcallId` is that
  each organization can have its own `organizationPortcallId` and multiple `organizationPortcallId`s
  can refer to the same visit, but that visit can only have one `localPortcallId`, issued by the port authority.
* `movementId`: this identifies a movement, which is a ship traveling from one location to another inside a port call
* `berthVisitId`: this identifies a berth visit, which is a ship being alongside a single berth
* `locationVisitId`: this identifies an anchor area visit, which is a ship being anchored in an anchor area of the port
* `serviceId`: this identifies a single service like bunkering

| ID                      | Format              |
|-------------------------|---------------------|
| localPortcallId         | `{UNLOCODE}{ID}`    |
| organizationPortcallId  | `PID-{SYSTEM}-{ID}` |
| movementId              | `MID-{SYSTEM}-{ID}` |
| berthVisitId            | `BID-{SYSTEM}-{ID}` |
| locationVisitId         | `LID-{SYSTEM}-{ID}` |
| serviceId               | `SID-{SYSTEM}-{ID}` |

`{UNLOCODE}` must be replaced by the UNLOCODE of the port the port call is taking place.

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
