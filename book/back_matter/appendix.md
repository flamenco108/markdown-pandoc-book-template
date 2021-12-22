# TEST

POST /roller/0?go=close HTTP/1.1
Host: 10.30.180.18
Content-Length: 0
 
HTTP/1.1 200 OK
Server: Mongoose/6.18
Connection: close
Content-Type: application/json
Content-Length: 212
 
{"state":"close","source":"http","power":0.00,"is_valid":true,"safety_switch":false,"overtemperature":false,"stop_reason":"normal","last_direction":"close","current_pos":26,"calibrating":false,"positioning":true}

POST /post HTTP/1.1
Content-Type: text/plain
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Cache-Control: no-cache
Postman-Token: 74e7f29f-763c-48a9-b6d8-63ca9aace81b
Host: echo.getpostman.com
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 256
 
Duis posuere augue vel cursus pharetra. In luctus a ex nec pretium. Praesent neque quam, tincidunt nec leo eget, rutrum vehicula magna.
Maecenas consequat elementum elit, id semper sem tristique et. Integer pulvinar enim quis consectetur interdum volutpat.
 
HTTP/1.1 200 OK
Date: Mon, 13 Dec 2021 21:48:20 GMT
Content-Type: text/plain
Content-Length: 50
Connection: keep-alive
Server: nginx
 
This service has moved to +