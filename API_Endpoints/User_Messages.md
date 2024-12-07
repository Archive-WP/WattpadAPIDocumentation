# User Messages:

Returns a list of user's conversations.

### URL:

**Sorted by date:** \
`https://www.wattpad.com/v4/users/{username}/messages/`

**Only Pinned:** \
`https://www.wattpad.com/v4/users/{username}/messages/latest/`

### Fields:

| Field | Data Type |
| - | - |
| messages | List ([Message](../Data_Types/Message.md)) |
| total | Int |
| nextUrl | URL |

### Error Codes:

- [NotFound](../General/Error_Codes.md#1014)
- [InvalidAction](../General/Error_Codes.md#1131)

### Example Usage:

`https://www.wattpad.com/v4/users/WattpadIndia/messages`

`https://www.wattpad.com/v4/users/WattpadOriginals/messages`