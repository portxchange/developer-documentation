# Integrating as an Carrier

Carrier can provide data about vessels visiting port, anchorages, berths, or terminals.

General overview of the PortXchange Exchange API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

## Event types

The API expects next the types of events:

```
anchorArea.eta.carrier -- an estimate time of arrival at anchorage
anchorArea.etd.carrier -- an estimate time of departure from anchorage
berth.ata.carrier -- an actual time of arrival at berth or terminal
berth.atd.carrier -- an actual time of departure from berth or terminal
berth.cancel.carrier -- a berth or terminal visit cancellation
berth.eta.carrier -- an estimate time of arrival at berth or terminal
berth.etd.carrier -- an estimate time of departure from berth or terminal
pilotBoardingPlace.ata.carrier -- an actual time of arrival at pilot boarding place
pilotBoardingPlace.atd.carrier -- an actual time of departure from pilot boarding place
pilotBoardingPlace.eta.carrier -- an estimate time of arrival at pilot boarding place
pilotBoardingPlace.etd.carrier -- an estimate time of departure from pilot boarding place
port.ata.carrier -- an actual time of arrival at port
port.atd.carrier -- an actual time of departure from port
port.cancel.carrier -- a port visit cancellation
port.eta.carrier -- an estimage time of arrival at port
port.etd.carrier -- an estimate time of departure from port
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