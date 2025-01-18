# Library:

Return stories from the user's library. \
**This endpoint requires authentication cookies**

### URL:

`https://www.wattpad.com/library?&_data=routes/_currentReads.library`

### Fields:

| Field | Data Type |
| - | - |
| title | String |
| libraryStories | [Library Resource](../Data_Types/Library_Resource.md)
| premiumPicks | null (I've never gotten anything but `null` from this) |
| isMobileCheck | Boolean |
| adEligibility	 | List(Unknown) (It's always been empty for me) |

### Example Usage:

`https://www.wattpad.com/library?&_data=routes/_currentReads.library`

`https://www.wattpad.com/library?&limit=2&offset=0&_data=routes/_currentReads.library`