# Content Settings:

Return the user's content settings. \
**This endpoint requires authentication cookies**

### URL:

`https://www.wattpad.com/v5/users/{literally anything}/content-settings`
**This endpoint is weird, the requests from https://wattpad.com will always use your username, but you can put literally any string in place of your username and it will still return *your* content settings info**

### Fields:

| Field | Data Type |
| - | - |
| includeMature | Boolean |
| unblockableTags | List (String) |
| tagLimit | Int |

### Error Codes:

- [PermissionDenied](../General/Error_Codes.md#1018)

### Example Usage:

`https://www.wattpad.com/v5/users/qwertyuiopasdfghjklzxcvbnm/content-settings`