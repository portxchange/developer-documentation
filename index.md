# Getting started

This page will provide you with all the information you need to connect to our APIs.

## Creating Port-Xchange account

To integrate with Port-Xchange API, you will need to register a company and create a developer account.

// TODO: Explain how

## Creating API keys

To ensure secure access to the data, we require automated systems to use authentication mechanisms based on API keys.

To successfully authorize your API requests, the developer has to create a set of API keys. 

An API Key and a company identifier will be required for every API call. The values are provided as HTTP headers.

More information about key management and security best practices can be found on the [Key management](key-management.md) page.

## Authorizing your API calls

Once created, API key can be used to authorize the API request.

Each API call must have the next HTTP headers:
- `X-Api-Key` - an API key created in the Developer Portal;
- `X-Company-Id` - a company ID.

The values for the headers can be found on the Developer Portal page.

Detailed guide can be found on the [Authorization](authorization.md) page.

## Sending data to Port-Xchange

Information about vessels and activities can be provided to Port-Xchange systems using Push API.
The API accepts information in form of events. 
The events must be submitted one at a time.

More detailed information is located on the [Getting started: Sending Data](/sending-data/index.md) page.

## Receiveing data from Port-Xchange

The event infomation for already finished portcalls can be received from Port-Xchange systems.
For the provided timeframe, the API will return a list of events of all port calls that were finished in the given period. Port calls in progress or planned port calls are not available for querying.

More detailed information is located on the [Getting started: Receiving data](/receiving-data/index.md) page.