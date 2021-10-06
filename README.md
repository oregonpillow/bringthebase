# bringthebase
Simple Base64 encoder / decoder. 
Inspired by https://www.base64encode.org


<ul><h3>Usage:</h3>
  
  ```python
from base64convert import base64_encode, base64_decode

test = 'This is a test string.'

encoded_test = base64_encode(test)
print(encoded_test)
>>> 'VGhpcyBpcyBhIHRlc3Qgc3RyaW5nLg=='

decoded = base64_decode(encoded_test)
print(decoded)
>>> 'This is a test string.'

```


# Reference 
https://en.wikipedia.org/wiki/Base64
