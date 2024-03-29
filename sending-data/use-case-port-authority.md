# Integrating as a Port Authority

Port Authority can provide data about vessels visiting port, anchorages, berths, or terminals, as well as bunkering operations, tug and pilot activities.

A general overview of the PortXchange Exchange API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

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
berth.ptd.portAuthority -- a planned time of departure from berth or terminal
bunkerService.atc.portAuthority -- an actual time of beggining of bunkering service
bunkerService.ats.portAuthority -- an actual time of end of bunkering service
bunkerService.cancel.portAuthority -- a cancellation of bunkering service
pilotBoardingPlace.pta.portAuthority -- a planned time of arrival at pilot boarding place
pilotDisembarked.at.portAuthority -- an actual time of pilot disembarkage 
pilotOnBoard.at.portAuthority -- an actual time of pilot getting on board
port.ata.portAuthority -- an actual time of arrival at port
port.atd.portAuthority -- an actual time of departure from port
port.cancel.portAuthority -- a port visit cancellation
port.clearance.portAuthority -- a port clearance event
port.eta.portAuthority -- an estimage time of arrival at port
port.etd.portAuthority -- an estimate time of departure from port
tugsFromBerth.reportnumber.portAuthority -- a number of tugs assisting outbound movement from berth or terminal, requires number of tugs in the event context
tugsNoMoreStandby.at.portAuthority
tugsNoMoreStandby.et.portAuthority
tugsStandby.at.portAuthority
tugsStandby.et.portAuthority
tugsToBerth.reportnumber.portAuthority -- a number of tugs assisting an inbound movement to berth or terminal, requires number of tugs in the event context
```

The full list of event types can be found in the [Exchange API Docs](https://portxchange.github.io/exchange-api-docs/#/routes/post-event).

## Locations

The location type field of the event payload can be populated with:

```
anchorArea -- when the event happens at the anchorage (anchorage visits)
berth -- if the exact berth is known at the moment of data submission (berth and terminal visits, bunkering  and pilot events)
terminal -- if the exact berth is not known at the moment of data submission (berth and terminal visits, bunkering and pilot events)
pilotBoardingPlace -- when the event happens at the pilot boarding place (pilot activity)
port - when providing port visit estimates and actuals
```

The full list of location types can be found in the [Exchange API Docs](https://portxchange.github.io/exchange-api-docs/#/routes/post-event).