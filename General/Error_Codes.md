# Error Codes:

### 462A:

Error Code: `462` \
Error Type: `ERROR` \
Message: `Too many parts; please request zip`

If too many parts are requested at once from [Part Content](../API_Endpoints/Part_Content.md), this error will be returned.

### 462B:

Error Code: `462` \
Error Type: `ERROR` \
Message: `Missing story_id`

If the `?story_id={Part ID}` parameter is not used with [Sync Reading Position](../API_Endpoints/Sync_Reading_Position.md), this error will be returned.

### 463:

Error Code: `463` \
Error Type: `ERROR` \
Message: `Could not find any parts for that story`

If a deleted or non-existent id is specified for [Part Content](../API_Endpoints/Part_Content.md), this error will be returned.

### 466:

Error Code: `466` \
Error Type: `ERROR` \
Message: `Invalid request method`

Honestly I'm not sure what triggers this, but going to `https://www.wattpad.com/apiv2/ignoreuser` causes it.

### 1001:

Error Code: `1001` \
Error Type: `InvalidEndpoint` \
Message: `API method not found`

If an invalid endpoint is specified, this error will be returned.

### 1005:

Error Code: `1005` \
Error Type: `InvalidValue` \
Message: `Invalid parameter value`

If non-existent fields are requested, this error will be returned. \
**NOTE: Not all endpoints will return this error for non-existent fields**

### 1006:

Error Code: `1006` \
Error Type: `RequiredParamMissing` \
Message: `Parameter missing`

If parameters an endpoint requires are missing, this error will be returned.

### 1011:

Error Code: `1011` \
Error Type: `NotFound` \
Message: `Reading list not found`

If a deleted or non-existent list is specified for [List Info](../API_Endpoints/List_Info.md), this error will be returned.

### 1014:

Error Code: `1014` \
Error Type: `NotFound` \
Message: `User not found`

If a deleted or non-existent user is specified for [User Info](../API_Endpoints/User_Info.md), [User Messages](../API_Endpoints/User_Messages.md), [User Stories](../API_Endpoints/User_Stories.md), [Following](../API_Endpoints/Following.md), or [Followers](../API_Endpoints/Followers.md), this error will be returned.

### 1017:

Error Code: `1017` \
Error Type: `NotFound` \
Message: `Story not found`

If a deleted or non-existent story is specified for [Story Info](../API_Endpoints/Story_Info.md), this error will be returned.

### 1018:

Error Code: `1018` \
Error Type: `PermissionDenied` \
Message: `User not logged in`

If [Blocks](../API_Endpoints/Blocks.md), [Content Settings](../API_Endpoints/Content_Settings.md), or [Wallet](../API_Endpoints/Wallet.md) is accessed without authentication cookies, this error will be returned.

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

### 1131:

Error Code: `1131` \
Error Type: `InvalidAction` \
message: `Conversations have been disabled on this profile.`

Attempting to use [User Messages](../API_Endpoints/User_Messages.md) on a user that has disabled conversations will return this error.

### 1154:

Error Code: `1154` \
Error Type: `AccessDenied` \
Message: `Access denied`

If [Blocks](../API_Endpoints/Blocks.md) is accessed without authentication cookies from the target user, this error will be returned.


### 1099:

Error Code: `1099` \
Error Type: `InternalError` \
Message: `Followers disabled`

Attempting to query a user's followers past 2000 returns this error.

### 2001:

Error Code: `2001` \
Error Type: `InternalError` \
Message: `Oops something went wrong, please try again later`

Invalid use of `?tags=` in [Hotlist](../API_Endpoints/Hotlist.md) returns this error.