<H2> Pronto Push API </H2>

This API is used to push events to Pronto infrastructure. User needs to provide request body based on the event which they want to push to the system .

Example request to use above API

```
curl --location --request POST '{HOST_NAME}/{ENV}/v1/share/push' \
--header 'X-Company-Id: XXX' \
--header 'Content-Type: application/json' \
--header 'x-api-key: XXX' \
--d '{"key1":"value1","key2":"value2"}'
```

+ HOST_NAME -> use host name for different env for test, accp and prod.
+ ENV -> Env can be test, accp and prod.
+ X-Company-Id -> company hash which is unique per company and will be visible in the developer portal.
+ X-Api-Key -> the api key which was created using developer portal.
+ BODY -> the event json which needs to be pushed to Pronto infrastructure.