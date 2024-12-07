# Error Codes:

### InvalidEndpoint:

Error Code: `1001` \
Error Type: `InvalidEndpoint` \
Message: `API method not found`

If an invalid endpoint is specified this error will be returned.

### NotFound:

Error Code: `1014` \
Error Type: `NotFound` \
Message: `User not found`

If a deleted or non-existent user is specified for [User Info](../API_Endpoints/User_Info.md), [User Following List](../API_Endpoints/User_Following_List.md), or [User Followers List](../API_Endpoints/User_Followers_List.md) this erorr will be returned.

### PermissionDenied

Error Code: `1062` \
Error Type: `PermissionDenied` \
message: `Not authorized to access API.  Go to developer.wattpad.com to get an API key.`

Honestly I'm not sure what triggers this, just that clicking Wattpad API URLs will always give me this until I click into the URL bar and then hit enter.

### InternalError:

Error Code: `1099` \
Error Type: `InternalError` \
Message: `Followers disabled`

Attempting to query a user's followers past 2000 returns this error.