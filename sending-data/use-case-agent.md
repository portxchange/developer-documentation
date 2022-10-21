# Integrating as an Agent

Agents can provide data about vessels visiting port, anchorages, berths, or terminals, as well as any planned activities for a vessel.

General overview of the PortXchange Exchange API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

## Event types

The API expects next the types of events:

```
anchorArea.ata.agent -- an actual time of arrival at anchorage
anchorArea.atd.agent -- an actual time of departure from anchorage
anchorArea.eta.agent -- an estimate time of arrival at anchorage
anchorArea.etd.agent -- an estimate time of departure from anchorage
berth.ata.agent -- an actual time of arrival at berth or terminal
berth.atd.agent -- an actual time of departure from berth or terminal
berth.cancel.agent -- a berth or terminal visit cancellation
berth.eta.agent -- an estimate time of arrival at berth or terminal
berth.etd.agent -- an estimate time of departure from berth or terminal
bunkerService.cancel.agent -- a cancellation of bunkering service
bunkerService.etc.agent -- an estimate time of beggining of bunkering service
bunkerService.ets.agent -- an estimate time of end of bunkering service
cargoOperations.cancel.agent -- a cancellation of cargo operations
cargoOperations.etc.agent -- an estimate time of cargo operations end
cargoOperations.ets.agent -- an estimate time of the beginning of cargo operations
movement.cancel.agent -- a cancellation of movement
pilotBoardingPlace.eta.agent -- an estimate time of arrival at pilot boarding place
pilotBoardingPlace.etd.agent -- an estimate time of departure from pilot boarding place
port.ata.agent -- an actual time of arrival at port
port.atd.agent -- an actual time of departure from port
port.cancel.agent -- a port visit cancellation
port.eta.agent -- an estimage time of arrival at port
port.etd.agent -- an estimate time of departure from port
repairService.cancel.agent -- a cancellation of repair operations
repairService.etc.agent -- an estmate time of repair service end
repairService.ets.agent -- an estmate time of beggining of repair service
slops.cancel.agent -- a cancellation of slops operations
slops.etc.agent -- an estmate time of slops service end
slops.ets.agent -- an estmate time of slops service start
stores.cancel.agent -- a cancellation of stores operations
stores.etc.agent -- an estmate time of stores operations end
stores.ets.agent -- an estmate time of stores operations start
tugsFromBerth.reportnumber.agent -- a number of tugs assisting outbound movement from berth or terminal, requires number of tugs in the event context
tugsToBerth.reportnumber.agent -- a number of tugs assisting inbound movement to berth or terminal, requires number of tugs in the event context
waste.cancel.agent -- a cancellation of waste operations
waste.etc.agent -- an estmate time of waste operations end
waste.ets.agent -- an estmate time of waste operations start
waterSupply.cancel.agent -- a cancellation of water supplies operations
waterSupply.etc.agent -- an estmate time of water supplies operations end
waterSupply.ets.agent -- an estmate time of water supplies operations start
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