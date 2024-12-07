### Fields:

| Field | Data Type |
|-|-|
| id | String |
| title | String |
| length | Int |
| createDate | UTC Time |
| modifyDate | UTC Time |
| voteCount | Int |
| readCount | Int |
| commentCount | Int |
| language | [Language](./Language.md) |
| user | [User](./User.md) |
| description | String |
| cover | URL |
| cover_timestamp | UTC Time |
| completed | Boolean |
| categories | List (Int) |
| tags | List (String) |
| rating | Int |
| mature | Boolean |
| copyright | Int |
| url | URL |
| firstPartId | Int |
| numParts | Int |
| firstPublishedPart | [Part](./Part.md) |
| lastPublishedPart | [Part](./Part.md) |
| parts | List ([Part](./Part.md)) |
| deleted | Boolean |