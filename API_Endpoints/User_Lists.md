# User Lists:

Returns a list of user's lists.

### URL:

`https://www.wattpad.com/api/v3/users/{username}/lists`

### Fields:

| Field | Data Type |
| - | - |
| lists | List ([List](../Data_Types/List.md)) |
| total | Int |

## Special Syntax:

`?non_empty=1` can be appended to return only lists with at least one story.

### Error Codes:

- [NotFound](../General/Error_Codes.md#1014)

### Example Usage:

`https://www.wattpad.com/api/v3/users/wattpad/lists`

`https://www.wattpad.com/api/v3/users/wattpadexplorer/lists`

`https://www.wattpad.com/api/v3/users/wattpad/lists?fields=lists(id,name)`