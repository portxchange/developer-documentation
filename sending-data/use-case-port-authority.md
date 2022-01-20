# Integrating as a Port Authority

Port Authority can provide data about vessels visiting port, anchorages, berths or terminals, as well as bunkering operations, tug and pilot activities.

A general overview of the Port-Xchange Push API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

## Event types

The API expects next the types of events:

```
anchorArea.eta.portAuthority -- an estimate time of arrival at anchorage
anchorArea.ata.portAuthority -- an actual time of arrival at anchorage
anchorArea.etd.portAuthority -- an estimate time of departure from anchorage
anchorArea.atd.portAuthority -- an actual time of departure from anchorage
berth.ata.portAuthority -- an actual time of arrival at berth or terminal
berth.atd.portAuthority -- an actual time of departure from berth or terminal
berth.cancel.portAuthority -- a berth or terminal visit cancellation
berth.eta.portAuthority -- an estimate time of arrival at berth or terminal
berth.etd.portAuthority -- an estimate time of departure from berth or terminal
berth.pta.portAuthority -- a planned time of arrival at berth or terminal
berth.ptd.portAuthority -- a planned time of departure from berth or terminal
bunkerService.atc.portAuthority -- an actual time of beggining of bunkering service
bunkerService.ats.portAuthority -- an actual time of end of bunkering service
bunkerService.cancel.portAuthority -- a cancellation of bunkering service
pilotBoardingPlace.eta.portAuthority --
pilotBoardingPlace.pta.portAuthority --
pilotDisembarked.at.portAuthority --
pilotOnBoard.at.portAuthority --
port.ata.portAuthority -- an actual time of arrival at port
port.atd.portAuthority -- an actual time of departure from port
port.cancel.portAuthority -- a port visit cancellation
port.eta.portAuthority -- an estimage time of arrival at port
port.etd.portAuthority -- an estimate time of departure from port
tugsStandby.et.portAuthority --
tugsStandby.at.portAuthority --
tugsNoMoreStandby.et.portAuthority -- 
tugsNoMoreStandby.at.portAuthority --
```
// TODO: check if the list is full, it should contain movements at least

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