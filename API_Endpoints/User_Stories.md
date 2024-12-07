# User Following List:

Returns a list of Wattpad users published stories.

### URL:

`https://www.wattpad.com/api/v3/users/{username}/stories`

### Fields:

| Field | Data Type |
| - | - |
| stories | list ([Story](../Data_Types/Story.md)) |
| total | Int |

### Error Codes:

- [NotFound](../General/Error_Codes.md#notfound)

### Example Usage:

`https://www.wattpad.com/api/v3/users/wattpad/stories`

`https://www.wattpad.com/api/v3/users/wattpadstories/stories`

`https://www.wattpad.com/api/v3/users/Wattpad/stories?fields=stories(id,title,user(username,description,numStoriesPublished))`