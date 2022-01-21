# Integrating as an Agent

Agents can provide data about vessels visiting port, anchorages, berths, or terminals, as well as any planned activities for a vessel.

General overview of the Port-Xchange Push API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

## Event types

The API expects next the types of events:

```
anchorArea.ata.agent
anchorArea.atd.agent
anchorArea.eta.agent
anchorArea.etd.agent
berth.ata.agent
berth.atd.agent
berth.cancel.agent
berth.eta.agent
berth.etd.agent
bunkerService.cancel.agent
bunkerService.etc.agent
bunkerService.ets.agent
cargoOperations.cancel.agent
cargoOperations.etc.agent
cargoOperations.ets.agent
movement.cancel.agent
pilotBoardingPlace.eta.agent
pilotBoardingPlace.etd.agent
port.ata.agent
port.atd.agent
port.cancel.agent
port.eta.agent
port.etd.agent
repairService.cancel.agent
repairService.etc.agent
repairService.ets.agent
slops.cancel.agent
slops.etc.agent
slops.ets.agent
stores.cancel.agent
stores.etc.agent
stores.ets.agent
tugsFromBerth.reportnumber.agent
tugsToBerth.reportnumber.agent
waste.cancel.agent
waste.etc.agent
waste.ets.agent
waterSupply.cancel.agent
waterSupply.etc.agent
waterSupply.ets.agent
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