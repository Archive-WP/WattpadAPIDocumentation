# Stories:

Returns stories in special lists

### URL:

`https://www.wattpad.com/api/v3/stories/`

### Fields:

| Field | Data Type |
| - | - |
| stories | List ([Story](../Data_Types/Story.md)) |
| total | Int |
| filter | String |
| nextUrl | URL |

### Special Syntax:

`?filter={Filter}` can be appended to the URL to switch which list to return stories from.

Possible values are:
- hot
- featured
- new

### Error Codes:

- [InvalidValue](../General/Error_Codes.md#1005)

### Example Usage:

`https://www.wattpad.com/api/v3/stories/237369078`

`https://www.wattpad.com/api/v3/stories/9341306`

`https://www.wattpad.com/api/v3/stories/9341306?fields=id,title,user(username)`