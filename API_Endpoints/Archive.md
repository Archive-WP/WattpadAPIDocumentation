# Archive:

Return stories from the user's archive. \
**This endpoint requires authentication cookies**

### URL:

`https://www.wattpad.com/archive?&_data=routes/_currentReads.archive`

### Fields:

| Field | Data Type |
| - | - |
| title | String |
| archiveStories | [Library Resource](../Data_Types/Library_Resource.md)
| premiumPicks | null (I've never gotten anything but `null` from this) |
| isMobileCheck | Boolean |
| adEligibility	 | List(Unknown) (It's always been empty for me) |

### Example Usage:

`https://www.wattpad.com/archive?&_data=routes/_currentReads.archive`

`https://www.wattpad.com/archive?&limit=2&offset=0&_data=routes/_currentReads.archive`