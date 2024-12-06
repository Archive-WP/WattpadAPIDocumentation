# User Info:

Returns info about a Wattpad user

### URL:

`https://www.wattpad.com/api/v3/users/{username}`

### Fields:

| Field | Data Type |
|-|-|
| username | String |
| avatar | URL |
| isPrivate	false | Boolean |
| backgroundUrl	| URL |
| follower | Boolean |
| following | Boolean |
| name | String |
| description | String |
| status | String |
| gender | String |
| genderCode | String |
| language | Int |
| locale | String |
| createDate | UTC Time |
| modifyDate | UTC Time |
| location | String |
| verified | Boolean |
| ambassador | Boolean |
| facebook | String |
| website | String |
| lulu | String |
| smashwords | String |
| bubok | String |
| votesRecieved | Int |
| numStoriesPublished | Int |
| numFollowing | Int |
| numFollowers | Int |
| numMessages | Int |
| numLists | Int |
| verified_email | Boolean |
| preferred_categories | List |
| allowCrawler | Boolean |
| deeplink | URL |
| isMuted | Boolean |

### Error Codes:

- [NotFound](./Error_Codes.md#notfound)

### Example Usage:

`https://www.wattpad.com/api/v3/users/wattpad`

`https://www.wattpad.com/api/v3/users/wattpadstories`

`https://www.wattpad.com/api/v3/users/WattpadExplorer?fields=username,description,numStoriesPublished`