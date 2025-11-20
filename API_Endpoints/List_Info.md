# User Info:

Returns info about a list

### URL:

`https://www.wattpad.com/api/v3/lists/{id}`

### Fields:

This endpoint returns a [List](../Data_Types/List.md).

### Error Codes:

- [NotFound](../General/Error_Codes.md#1011)

### Example Usage:

`https://www.wattpad.com/api/v3/lists/829974064`

`https://www.wattpad.com/api/v3/lists/1556841608`

`https://www.wattpad.com/api/v3/lists/829974064?fields=id,name,user(name)`

### IMPORTANT NOTE:

There exists a (bug?) in this endpoint that reveals extra metadata. Some stories, when requested using this endpoint, will contain metadata for deleted parts. These parts will include the unique `deleted` boolean field, which is set to `true`.

Requesting part content for parts with `deleted` set to `true` using [Part Content](./Part_Content.md) will result in error [463A](../General/Error_Codes.md#463A).

Compare these two requests. The first one returns metadata about story `91824688`. The second return metadata about list `277998770`, which contains story `91824688`. The [Story Info](./Story_Info.md) endpoint returns 22 parts for story `91824688`, whereas the [List Info](./List_Info.md) endpoint returns 26 parts. The 4 additional parts have the `deleted` field set to `true`.

`https://www.wattpad.com/api/v3/stories/91824688?fields=id,title,parts(id,title)`

`https://www.wattpad.com/api/v3/lists/277998770?fields=stories(id,title,parts(id,title,deleted))`