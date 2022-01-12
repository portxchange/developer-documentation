<H2> Pronto Event API </H2>

This API is use to fetch all the events per portcall. User need to provide the time start with following query parameters.

- from -> Timestamp to fetch portcalls events, portcalls started on or after this timestamp.
    * requered 
    * format -> `YYYY-MM-ddTHH:mm:ssZ`
    * example -> `2021-10-12T13:00:00Z` 

<br/>
- to -> Timestamp to fetch portcall events, portcalls ended on or before this timestamp.
    * optional (current timestamp if not provided) 
    * format -> `YYYY-MM-ddTHH:mm:ssZ`
    * example -> `2021-10-12T13:00:00Z` 


Example request to use above API

```
curl --location --request GET '{HOST_NAME}/{ENV}/api/v1/share/pull?from=2021-10-12T13%3A00%3A00Z&to=2021-10-12T17%3A00%3A00Z' \
--header 'X-Company-Id: XXX' \
--header 'Content-Type: application/json' \
--header 'x-api-key: XXX'
```

+ HOST_NAME -> use host name for different env for test, accp and prod.
+ ENV -> Env can be test, accp and prod.
+ X-Company-Id -> you can find under your keys.
+ X-Api-Key -> you can find under your keys.