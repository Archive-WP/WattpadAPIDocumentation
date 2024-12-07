# Search Stories:

Returns a list of stories based on the input.

### URL:

`https://www.wattpad.com/v4/search/stories/?query={input}`

### Fields:

| Field | Data Type |
| - | - |
| total | Int |
| stories | List ([Story](../Data_Types/Story.md)) |
| categories | List ([Category](../Data_Types/Category.md)) |
| tags | List ([Tag](../Data_Types/Tag.md)) |
| nextUrl | URL |

### Special Syntax:

There is special search parameter syntax for this endpoint.

The general syntax is a follows: \
`{URL}&{Filters}`

`URL` is the endpoint URL to make a request to. \
`Filters` is an ampersand (`&`) separated list of filter names and values. \
See [Example Usage](./Search_Stories.md#example-usage) for further details.

**Filters:**

| Filter | Data Type |
| - | - |
| filter | String (complete) |
| updateYoungerThan | Int (Num days) |
| minParts | Int |
| maxParts | Int |
| paid | Int (Boolean) |

### Example Usage:

`https://www.wattpad.com/v4/search/stories/?query=wattpad`

`https://www.wattpad.com/v4/search/users/?query=github`

`https://www.wattpad.com/v4/search/stories/?query=test&filter=complete&updateYoungerThan=30&maxParts=3`