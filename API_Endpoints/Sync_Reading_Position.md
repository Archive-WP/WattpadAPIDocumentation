# Sync Reading Position:

Returns the reading progress of a book. \
**NOTE: This endpoint requires authentication cookies to return non-empty values**

### URL:

`https://www.wattpad.com/apiv2/syncreadingposition?story_id={Part ID}` \
**NOTE: `PART ID` is required and must be a part ID of any part in the target story.**

### Fields:

| Field | Data Type |
| - | - |
| part | Int |
| position | String |

### Error Codes:

- [462](../General/Error_Codes.md#462B)

### Example Usage:

`https://www.wattpad.com/apiv2/syncreadingposition?story_id=939059907`

`https://www.wattpad.com/apiv2/syncreadingposition?story_id=939081431`

`https://www.wattpad.com/apiv2/syncreadingposition?story_id=939103774`