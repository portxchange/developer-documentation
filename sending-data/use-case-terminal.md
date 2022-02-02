# Integrating as a Terminal

Terminals can provide data about vessels visiting their berths.

API expects events containing data of estimated or actual times of arrival and depature and cargo operation schedules.

A general overview of the Port-Xchange Push API can be found on [Getting started: Sending Data](/sending-data/index.md) page.

## Event types

The API expects next the types of events:

```
berth.ata.terminal -- an actual time of arrival at berth
berth.atd.terminal -- an actual time of departure from berth
berth.cancel.terminal -- a cancellation of a terminal or berth visit
berth.eta.terminal -- an estimate time of arrival at berth
berth.etd.terminal -- an estimate time of departure from berth
berth.pta.terminal -- a planned time of arrival at berth
berth.ptd.terminal -- a planned time of departure from berth
cargoOperations.atc.terminal -- an actual time of cargo operations end
cargoOperations.ats.terminal -- an actual time of the beginning of cargo operations
cargoOperations.etc.terminal -- an estimate time of cargo operations end
cargoOperations.ets.terminal -- an estimate time of the beginning of cargo operations
surveyor.atc.terminal -- an actual time of surveyor operations end
surveyor.ats.terminal -- an actual time of the beginning of surveyor operations
```

The full list of event types can be found in the [specification](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L215-L340)

## Locations

The location type field of the event payload can be populated with:

```
berth -- if the exact berth is known at the moment of data submission
terminal -- if the exact berth is not known at the moment of data submission
```

The full list of event types can be found in the [specification](https://github.com/PortCallOptimisation/port-call-event-format/blob/master/Event_spec.ts#L343-L352)
