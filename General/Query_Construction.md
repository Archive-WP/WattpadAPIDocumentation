# Query Construction:

## Fields:

The Wattpad API does not always return all possible fields and sometimes you might want to only receive specific fields.

To gain finer control over what fields a query returns, you can modify a URL to request only certain fields.

The general syntax is as follows: \
`{URL}?fields={Fields}`

`URL` is the endpoint URL to make a request to. \
`Fields` is a comma-separated list of every field you wish to receive.

### Example Queries:

`https://www.wattpad.com/api/v3/users/Wattpad?fields=username,description,numStoriesPublished`

`https://www.wattpad.com/api/v3/users/WattpadExplorer/followers?fields=users(username,backgroundURL,description,numFollwers)`

## NextURL, Limit, and Offset:

By default, when making queries that return lists as the primary data type (E.G. [User Following List](../API_Endpoints/User_Following_List.md) and [User Followers List](../API_Endpoints/User_Followers_List.md)), Wattpad will only return the first 10 items. The `nextUrl` field is an automatically generated URL from Wattpad that utilizes `limit` and `offset` to provide the next set of items.

`nextUrl`'s `limit` value will be the same as the current request's `limit`.

`nextUrl`'s `offset` value will be the current request's `limit` and `offset` valued added together.

However, `limit` and `offset` can be manually used to gain greater control over how what data is requested from the Wattpad API.

`offset` specifies how far into the list the returned items should start from. \
**Note: `offset` is zero-indexed**

`limit` specifies the maximum number of items that will be returned.

The general syntax for `limit` and `offset` is as follows: \
`{URL}?limit={limit value}?offset={offset value}`

It is not required to use both at once, and if one or both are omitted then the default values will be used.

The default for `limit` is 10. \
Ehe default for `offset` is 0.

### Example Queries:

`https://www.wattpad.com/api/v3/users/wattpad/following?limit=5&offset=10`

will return the 10th to 15th users, and it's `nextUrl` will be

`https://www.wattpad.com/api/v3/users/wattpad/following?limit=5&offset=15`
\
\
\
`https://www.wattpad.com/api/v3/users/wattpad/following?limit=2&offset=30`

will return the 30th to 32nd users, and it's `nextUrl` will be

`https://www.wattpad.com/api/v3/users/wattpad/following?limit=5&offset=15`