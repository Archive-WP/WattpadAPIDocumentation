# User Info:

Returns info about a list

### URL:

`https://www.wattpad.com/api/v3/lists/{id}`

### NOTE:

There is a bug(?) is this endpoint where metadata for deleted parts is returned, this metadata is not returned from any other endpoint. \
An example list where is occurs is `829974064`. In this this, story `181121904` is shown to have an extra chapter `855649155`. \
This chapter is not returned using [Story Info](./Story_Info.md). \
These additional deleted parts have the field `deleted` set to `true`. 

### Fields:

This endpoint returns a [List](../Data_Types/List.md).

### Error Codes:

- [NotFound](../General/Error_Codes.md#1011)

### Example Usage:

`https://www.wattpad.com/api/v3/lists/829974064`

`https://www.wattpad.com/api/v3/lists/1556841608`

`https://www.wattpad.com/api/v3/lists/829974064?fields=id,name,user(name)`