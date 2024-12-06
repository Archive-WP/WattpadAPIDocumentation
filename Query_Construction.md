# Query Construction:

The Wattpad API does not always return all possible fields and sometimes you might want to only receive specific fields.

To gain finer control over what fields a query returns, you can modify a URL to request only certain fields.

The general syntax is as follows: \
`{URL}?fields={Fields}`

`URL` is the endpoint URL to make a request to. \
`Fields` is a comma-separated list of every field you wish to receive.

### Example Queries:

`https://www.wattpad.com/api/v3/users/Wattpad?fields=username,description,numStoriesPublished`

`https://www.wattpad.com/api/v3/users/WattpadExplorer/followers?fields=users(username,backgroundURL,description,numFollwers)`