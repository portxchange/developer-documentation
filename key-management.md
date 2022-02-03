# Key Management

To enable access to Port-Xchange APIs, the API Key-based authorization is used.
The developers can create and manage API keys using the Developer Portal. The Developer Portal is accessible from the Synchronizer application.

## Accessing the Developer Portal

To access the Developer Portal, the registered Synchronizer user must have the Developer role.

Once logged in, the developer can open the side menu with the hamburger button and find a link to 'Developer Portal'. The link will open Developer Portal and allow API key management for the company.

![side menu](/images/side-menu.png)

If the Developer Portal is not present in the side menu, please, verify that the user has a Developer role. After changing roles for the user, the user has to re-login into Synchronizer.

## Creating API keys

To create an API Key, a developer has to open the Developer Portal.

1. Navigate to the block named `Create API key`
1. Enter the API Key name. It must be unique and can contain any alphanumeric characters, as well as symbols.
1. Click `Generate API key`. The validation message may appear. If it does, check the input and repeat.
1. If successful, the API key will appear in the `Your API key` field.
1. Copy the API key and store it securely.

**Attention!** 
The API key is displayed only once after creating. It cannot be retrieved again after creating. 
If you lost your API key, consider deleting it and creating a new one instead.

<img src="/images/key-form.png" alt="key form" width="518" height="577" />

## Revoking and deleting API keys

To revoke or delete an API key, a developer has to open the Developer Portal.

1. Navigate to the block named `Generated API keys`.
1. In the list of keys find the wanted key.
1. Place the mouse pointer on top of the row containing the wanted key. The 3-dot menu will appear.
1. In the 3-dot menu find the corresponding button: `Revoke API key` or `Remove from list`. Click on the option you need.
1. The confirmation dialog will appear. Confirm the action if it is correct.

Revoked keys stay in the list of keys. Deleted keys disappear from the list and won't be shown in the future. A revoked key can be deleted later.
API calls with both, revoked and deleted, keys will not pass authorization.

**Attention!** 
Revocation or deletion cannot be undone. Be careful when invalidating keys, verify that it won't affect production systems.

![removing keys](/images/removing-keys.png)

## Security best practices

1. Do not publish API keys in your source code. If a key is exposed in a source file, consider revoking it and generating a substitution.
1. Use a separate key for each automated system. In the event of key exposure, the affected systems will be limited to one that used that key.
1. Rotate the keys. The suggested frequency is every 3 or 6 months.
1. Review the keys. If the key is not used anymore, consider revoking and deleting them. Dangling keys pose a security risk.
