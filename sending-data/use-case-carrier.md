# Integrating as an Carrier

Carrier can provide data about vessels visiting port, anchorages, berths, or terminals.

General overview of the Port-Xchange Push API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

## Event types

The API expects next the types of events:

```
anchorArea.eta.carrier
anchorArea.etd.carrier
berth.ata.carrier
berth.atd.carrier
berth.cancel.carrier
berth.eta.carrier
berth.etd.carrier
pilotBoardingPlace.ata.carrier
pilotBoardingPlace.atd.carrier
pilotBoardingPlace.eta.carrier
pilotBoardingPlace.etd.carrier
port.ata.carrier
port.atd.carrier
port.cancel.carrier
port.eta.carrier
port.etd.carrier
```

The full list of event types can be found in the [specification](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L215-L340)

## Locations

The location type field of the event payload can be populated with:

```
anchorArea -- when the event happens at the anchorage (anchorage visits)
berth -- if the exact berth is known at the moment of data submission (berth and terminal visits, bunkering  and pilot events)
terminal -- if the exact berth is not known at the moment of data submission (berth and terminal visits, bunkering and pilot events)
pilotBoardingPlace -- when the event happens at the pilot boarding place (pilot activity)
port - when providing port visit estimates and actuals
```

The full list of event types can be found in the [specification](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L343-L352)