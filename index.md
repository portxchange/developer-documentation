# Getting started

This page will provide you with all the information you need to connect to our API(s).

## Creating PortXchange account

To integrate with PortXchange's API, you will need to register a company and create a developer account.

If you still don't have an account, please, contact us using [this form](https://port-xchange.com/contact/).

## Creating API keys

To ensure secure access to the data, we require automated systems to use authentication mechanisms based on API keys.

To successfully authorize your API requests, the developer has to create a set of API keys. 

An API Key and a company identifier will be required for every API call. The values are provided as HTTP headers.

More information about key management and security best practices can be found on the [Key management](key-management.md) page.

## Authorizing your API calls

Once created, your API key can be used to authorize the API request.

Each API call must have the next HTTP headers:
- `X-Api-Key` - an API key created in the Developer Portal;
- `X-Company-Id` - a company ID, unique per environment, can be found in the Developer Portal.
- `Content-Type`:`application/json` 

The values for the first two headers can be found on the Developer Portal page.

A detailed guide can be found on the [Authorization](authorization.md) page.

## Sending data to PortXchange

Information about vessels and activities can be provided to PortXchange systems
using the Exchange API. This API accepts information in form of events. The events
must be submitted one at a time.

More detailed information can be found in [Getting started: Sending Data](/sending-data/index.md).

## Receiving data from PortXchange

Besides sending data to PortXchange, it is also possible to retrieve data from our systems
using the Exchange API. Currently, there are a few endpoints through which data can be queried.

More detailed information can be found in [Getting started: Receiving data](/receiving-data/index.md).

## Changelog

Important updates for the APIs will be published on the [Changelog](changelog.md) page.
