# Following:

Returns part content. \
**NOTE: This endpoint requires authentication cookies in order to access paid story content**

### URL:

`https://www.wattpad.com/apiv2/?m=storytext&id={part_id}`

**OR**

`https://www.wattpad.com/apiv2/?m=storytext&group_id={story_id}` \
**NOTE: This format will download ALL parts for the specified story**

### Fields:

**Raw:**

This endpoint returns raw part content

**JSON:**

| Field | Data Type |
| - | - |
| text | String |
| text_hash | String |

**zip:**

This endpoint returns part content in a `.zip` file

### Special Syntax:

`&output={mode}` can be appended to the request to specify what format to download part content as.

There are two special modes that can be specified:

- json
- zip

If no `output` mode if specified, part content will be downloaded in raw form.

### Error Codes:

- [462](../General/Error_Codes.md#462)
- [463](../General/Error_Codes.md#463)

### Example Usage:

`https://www.wattpad.com/apiv2/?m=storytext&id=939103774`

`https://www.wattpad.com/apiv2/?m=storytext&id=512974613`

`https://www.wattpad.com/apiv2/?m=storytext&group_id=237369078&output=zip`