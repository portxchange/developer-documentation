# Integrating as an Service Provider

Service providers can send data about their planned and actual activities. 
It includes estimate and actual dates of the beginning end finishing the service and calncellation events.

General overview of the PortXchange Exchange API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

## Event types

The API expects next the types of events:

```
bunkerService.atc.serviceProvider
bunkerService.ats.serviceProvider
bunkerService.cancel.serviceProvider
bunkerService.etc.serviceProvider
bunkerService.ets.serviceProvider
cargoOperations.cancel.serviceProvider
cargoOperations.etc.serviceProvider
cargoOperations.ets.serviceProvider
provision.atc.serviceProvider
provision.ats.serviceProvider
provision.cancel.serviceProvider
provision.etc.serviceProvider
provision.ets.serviceProvider
repairService.atc.serviceProvider
repairService.ats.serviceProvider
repairService.etc.serviceProvider
repairService.ets.serviceProvider
slops.cancel.serviceProvider
slops.etc.serviceProvider
slops.ets.serviceProvider
stores.cancel.serviceProvider
stores.etc.serviceProvider
stores.ets.serviceProvider
surveyor.cancel.serviceProvider
surveyor.etc.serviceProvider
surveyor.ets.serviceProvider
waste.atc.serviceProvider
waste.ats.serviceProvider
waste.cancel.serviceProvider
waste.etc.serviceProvider
waste.ets.serviceProvider
waterSupply.cancel.serviceProvider
waterSupply.etc.serviceProvider
waterSupply.ets.serviceProvider
```

The full list of event types can be found in the [Exchange API Docs](https://portxchange.github.io/exchange-api-docs/#/routes/post-event).

## Locations

The location type field of the event payload can be populated with:

```
berth -- if the exact berth is known at the moment of data submission (berth and terminal visits, bunkering  and pilot events)
terminal -- if the exact berth is not known at the moment of data submission (berth and terminal visits, bunkering and pilot events)
```

The full list of location types can be found in the [Exchange API Docs](https://portxchange.github.io/exchange-api-docs/#/routes/post-event).