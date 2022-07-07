# How to read/parse web logs

Reading logs:
IPv4 address: 3digits.upto3digits.upto3digits.upto3digits, 0-255
Timestamp: could have Day/Month/Year, Year/Month/Day:hour:min:sec
HTTP Methods (verbs): GET is download, POST is upload
Endpoint or URI (the part of a URL after the domain): /api/v1 or something similar.
Endpoint example: 
- URL: https://ds.codeup.com/anomaly-detection/discrete-probabilistic-methods/
- Endpoint: /anomaly-detection/discrete-probabilistic-methods/
- Query String: When you see a question mark in url like ?page=7. Or youtube.com/watch?v=456789, so ?v=456789 is the query string. ?page=2&items_per_page=25
- HTTP Status Code: The status code a server returns on request. 
    - 404 not found, 403 forbidden
    - 500 errors are server errors
- Bytes transfered, as an integer
- User agent string is the identifier for the client (browser), ex "python-requests/2.21.0" 
or "Mozilla/5.0 (Linux; {Android Version}; {Build Tag etc.}) AppleWebKit/{WebKit Rev} (KHTML, like Gecko)
Chrome/{Chrome Rev} Mobile Safari/{WebKit Rev}" tells you about someone's browser


173.173.113.51 - - [17/Apr/2019:01:40:07 +0000] "GET /api/v1/sales?page=7 HTTP/1.1" 200 500637 "-" "python-requests/2.21.0"