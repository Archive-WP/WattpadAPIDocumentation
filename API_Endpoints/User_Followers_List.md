# User Followers List:

Returns a list of Wattpad users that are following a user

### URL:

`https://www.wattpad.com/api/v3/users/{username}/followers`

### Fields:

| Field | Data Type |
| - | - |
| users | List ([User](../Data_Types/User.md)) |
| total | Int |
| nextUrl | URL |

### Error Codes:

- [NotFound](../General/Error_Codes.md#1014)
- [InternalError](../General/Error_Codes.md#1099)

### Example Usage:

`https://www.wattpad.com/api/v3/users/wattpad/followers`

`https://www.wattpad.com/api/v3/users/wattpadstories/followers`

`https://www.wattpad.com/api/v3/users/WattpadExplorer/followers?fields=users(username,description,numStoriesPublished)`