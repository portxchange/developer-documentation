# Authorization

To enable access to Port-Xchange APIs, the API Key-based authorization is used.
API Key management is available for users with the Developer role in Synchronizer. 
Check [Key Management](/key-management.md) page for detailed information on key management.

## How to

To authorize API call, the requester has to provide special headers:

- `X-Api-Key` - an API key created in the Developer Portal
- `X-Company-Id` - a company ID.

A company ID can be found on the Developer Portal page below the key creation form.

<img src="/images/key-form.png" alt="key form" width="518" height="577" />

*Attention!* 
For each environment, you must create a separate set of credentials.

Use the example shell-script to check your credentials:

```shell
curl --location --request GET 'https://exchange.port-xchange.com/test/v1/api/events?from=2021-10-12T13%3A00%3A00Z&to=2021-10-12T17%3A00%3A00Z' \
  --header 'Content-Type: application/json' \ 
  --header 'Accepts: application/json' \
  --header 'X-Company-Id: $YOUR_COMPANY_ID' \
  --header 'X-Api-Key: $YOUR_API_KEY'
```

Or, alternatively, in Python:

```python
import requests

headers = {
  'Content-Type': 'application/json',
  'Accepts': 'application/json',
  'X-Company-Id': 'YOUR_COMPANY_ID',
  'X-Api-Key': 'YOUR_API_KEY'
}
requests.get('https://exchange.port-xchange.com/test/v1/api/events?from=2021-10-12T13%3A00%3A00Z&to=2021-10-12T17%3A00%3A00Z', headers = headers)
```

For more examples, check the [Getting started: Receiving data](/receiving-data/index.md) or [Getting started: Sending Data](/sending-data/index.md) guides or Python and Shell scripts in [resources](/resources).
