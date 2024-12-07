# Lists:

Return stories from the Hot list.

### URL:

`https://api.wattpad.com/v5/hotlist?tags={Tag}`

### Fields:

| Field | Data Type |
| - | - |
| stories | List ([Story](../Data_Types/Story.md)) |
| total | Int |
| nextUrl | URL |

### Special Syntax:

`?tags={Tag}` is a **required** parameter for this endpoint

`&language={Language Code}` can be appended to filter by language

### Error Codes:

- [InternalError](../General/Error_Codes.md#2001)

### Example Usage:

`https://api.wattpad.com/v5/hotlist?tags=romance`

`https://api.wattpad.com/v5/hotlist?tags=teen`

`https://api.wattpad.com/v5/hotlist?tags=lgbtq&language=3`