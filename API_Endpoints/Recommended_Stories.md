# Recommended Stories:

Returns a list of recommend stories based on a story.

### URL:

`https://www.wattpad.com/api/v3/stories/{id}/recommended`

### Fields:

This endpoint returns a list of [Stories](../Data_Types/Story.md).

### Error Codes:

- [NotFound](../General/Error_Codes.md#1017)

### Example Usage:

`https://www.wattpad.com/api/v3/stories/237369078/recommended`

`https://www.wattpad.com/api/v3/stories/9341306/recommended`

`https://www.wattpad.com/api/v3/stories/9341306/recommended?fields=id,title,user(username)`