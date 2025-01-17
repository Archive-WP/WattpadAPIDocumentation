# Wallet:

Returns info about the user's coin wallet \
**NOTE: This endpoint requires authentication cookies**

### URL:

`https://www.wattpad.com/v5/users/{literally anything}/wallet`

**This endpoint is really weird, the requests from https://wattpad.com will always use your username, but you can put literally any string in place of your username and it will still return *your* wallet info**

### Fields:

| Field | Data Type |
| - | - |
| id | String |
| amount | Int |

### Error Codes:

- [PermissionDenied](../General/Error_Codes.md#1018)

### Example Usage:

`https://www.wattpad.com/v5/users/aaaaaaaaaaaaaaahsfuivhuqefiowbhuioohibhviuhmfivwgfvb/wallet`