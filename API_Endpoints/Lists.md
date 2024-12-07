# Lists:

Search for lists.

### URL:

`https://www.wattpad.com/v4/lists/?query={Query}`

### Fields:

| Field | Data Type |
| - | - |
| lists | List ([List](../Data_Types/List.md)) |
| total | Int |
| nextUrl | URL |

### Special Syntax:

`?query={Query}` is a **required** parameter for this endpoint

### Error Codes:

- [InvalidValue](../General/Error_Codes.md#1005)

### Example Usage:

`https://www.wattpad.com/v4/lists/?query=test`

`https://www.wattpad.com/v4/lists/?query=wattpad`

`https://www.wattpad.com/v4/lists/?query=id&fields=lists(id,name)`