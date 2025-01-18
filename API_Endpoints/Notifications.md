# Notifications:

Return the user's notifcations. \
**This endpoint requires authentication cookies**

### URL:

`https://www.wattpad.com/notifications?&_data=routes/notifications`

### Fields:

| Field | Data Type |
| - | - |
| title | String |
| notifications | [Notifications Resource](../Data_Types/Notifications_Resouce.md)
| followRequests | [Follow Requests Resource](../Data_Types/Follow_Requests_Resource.md) |
| siteRoot | URL |
| locale | String |
| currentUser | [User](../Data_Types/User.md) |
| mutedUsersList | List ([User](../Data_Types/User.md)) |
| adEligibility	 | List(Unknown) (It's always been empty for me) |

### Example Usage:

`https://www.wattpad.com/notifications?&_data=routes/notifications`