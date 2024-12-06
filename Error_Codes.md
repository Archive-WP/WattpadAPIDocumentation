# Error Codes:

### InvalidEndpoint:

Error Code: `1001` \
Error Type: `InvalidEndpoint` \
Message: `API method not found`

If an invalid endpoint is specified for `https://www.wattpad.com/api/v3/{endpoint}` this error will be returned.

### NotFound:

Error Code: `1014` \
Error Type: `NotFound` \
Message: `User not found`

If a deleted or non-existent user is specified for [User Info](./User_Info.md), [User Following List](./User_Following_List.md), or [User Followers List](./User_Followers_List.md) this erorr will be returned.

### InternalError:

Error Code: `1099` \
Error Type: `InternalError` \
Message: `Followers disabled`

Attempting to query a user's followers past 2000 returns this error.