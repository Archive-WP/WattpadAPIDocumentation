# Error Codes:

### 463:

Error Code: `463` \
Error Type: `ERROR` \
Message: `Could not find any parts for that story`

If a deleted or non-existent part is specified for [Part Content](../API_Endpoints/Part_Content.md), this error will be returned.

### 1001:

Error Code: `1001` \
Error Type: `InvalidEndpoint` \
Message: `API method not found`

If an invalid endpoint is specified, this error will be returned.

### 1005:

Error Code: `1005` \
Error Type: `InvalidValue` \
Message: `Invalid parameter value`

If no fields are requested, this error will be returned.

### 1011:

Error Code: `1011` \
Error Type: `NotFound` \
Message: `Reading list not found`

If a deleted or non-existent list is specified for [List Info](../API_Endpoints/List_Info.md), this error will be returned.

### 1014:

Error Code: `1014` \
Error Type: `NotFound` \
Message: `User not found`

If a deleted or non-existent user is specified for [User Info](../API_Endpoints/User_Info.md), [User Following List](../API_Endpoints/User_Following_List.md), or [User Followers List](../API_Endpoints/User_Followers_List.md), this error will be returned.

### 1017:

Error Code: `1017` \
Error Type: `NotFound` \
Message: `Story not found`

If a deleted or non-existent story is specified for [Story Info](../API_Endpoints/Story_Info.md), this error will be returned.

### 1020:

Error Code: `1020` \
Error Type: `NotFound` \
Message: `Story part not found`

If a deleted or non-existent part is specified for [Part Info](../API_Endpoints/Part_Info.md), this error will be returned.

### 1062:

Error Code: `1062` \
Error Type: `PermissionDenied` \
message: `Not authorized to access API.  Go to developer.wattpad.com to get an API key.`

Honestly I'm not sure what triggers this, just that clicking Wattpad API URLs will always give me this until I click into the URL bar and then hit enter.

### 1099:

Error Code: `1099` \
Error Type: `InternalError` \
Message: `Followers disabled`

Attempting to query a user's followers past 2000 returns this error.