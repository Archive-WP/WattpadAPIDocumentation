**THIS DATA TYPE IS NOT REALLY A DATA TYPE, IT CAN BE ONE OF MANY THINGS, DEPENDING ON THE NOTIFICATION TYPE**

### Fields (upload):

| Field | Data Type |
|-|-|
| story | [Story](./Story.md) |
| notification_instance_id | String |
| highlight_colour | String |

### Fields (inline_comment):

| Field | Data Type |
|-|-|
| comment | [Inline Comment](./Inline_Comment.md) |
| story | [Story](./Story.md) |
| notification_instance_id | String |
| highlight_colour | String |

### Fields (message):

| Field | Data Type |
|-|-|
| message | [Message](./Message.md) |
| notification_instance_id | String |
| highlight_colour | String |

### Fields (generic):

| Field | Data Type |
|-|-|
| icon | String |
| subtype | String |
| body | String |
| images | [Images Resource](./Images_Resource.md) |
| callToActionUrl | [Call To Action URL](./Call_To_Action_URL.md) |
| notification_instance_id | String |