# User Following List:

Returns a list of Wattpad users that a user follows

### URL:

`https://www.wattpad.com/api/v3/users/{username}/following`

### Fields:

| Field | Data Type |
| - | - |
| users | list ([User](../Data_Types/User.md)) |
| total | Int |
| nextUrl | URL |

### Error Codes:

- [NotFound](../General/Error_Codes.md#1014)

### Example Usage:

`https://www.wattpad.com/api/v3/users/wattpad/following`

`https://www.wattpad.com/api/v3/users/wattpadstories/following`

`https://www.wattpad.com/api/v3/users/WattpadExplorer/following?fields=users(username,description,numStoriesPublished)`