# User Reading Lists:

Returns a list of the user's lists \
**NOTE: This endpoint requires authentication cookies** \
**NOTE: Accessing this endpoint without authentication cookies will return `NULL`**

### URL:

`https://www.wattpad.com/resource/user_reading_lists?readingLists=true`

### Fields:

| Field | Data Type |
| - | - |
| ok | Boolean |
| data | Data ([Data](../Data_Types/Data.md)) |

### Example Usage:

`https://www.wattpad.com/resource/user_reading_lists?readingLists=true`