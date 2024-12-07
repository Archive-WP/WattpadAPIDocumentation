# Paid Content:

Returns paid story metadata.

### URL:

`https://www.wattpad.com/v5/story/{story_id}/paid-content/metadata?parts={Parts}`
**NOTE: `Parts` is a comma-separated list of part IDs belonging to the specified story**

### Fields:

| Field | Data Type |
|-|-|
| story | [Paid Story](../Data_Types/Paid_Story.md) |
| story | List [Paid Part](../Data_Types/Paid_Part.md) |

### Example Usage:

`https://www.wattpad.com/v5/story/236191234/paid-content/metadata?parts=985026173,986447974,986498548`

`https://www.wattpad.com/v5/story/215093947/paid-content/metadata?parts=842528199,842528909,842530852`