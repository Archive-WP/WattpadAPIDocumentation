# Blocks:

Returns a list of blocked users

### URL:

`https://www.wattpad.com/v4/users/{username}/blocks`

### Fields:

This endpoint returns a list of [Users](../Data_Types/User.md).

### Error Codes:

- [PermissionDenied](../General/Error_Codes.md#1018)
- [AccessDenied](../General/Error_Codes.md#1154)

### Example Usage:

`https://www.wattpad.com/v4/users/wattpad/blocks` **<- This will give error 1154!**