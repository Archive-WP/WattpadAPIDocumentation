This repo is mainly about endpoints to make HTTP GET requests to in order to receive JSON, and authentication is beyond that scope as it uses an HTTP POST request, but considering how important authentication is, here's some documentation about it.

To receive authentication cookies from Wattpad, an HTTP POST request must be made to\
`https://www.wattpad.com/auth/login?&_data=routes%2Fauth.login`\
with the data payload\
`username={username/email}&password={password}`

If the POST request is successful, the response will contain authentication cookies that may be used to make authenticated GET requests.

Example implementation in Python using the `requests` library can be found [here](./Authentication_Example.py)