# bringthebase
Simple Base64 encoder /decoder. 
Currently working on adding ability to use arbitrary base set of users' choosing.


<ul><h3>Usage:</h3>
  
  ```python
from base64convert import base64_encode, base64_decode

test = """Man is distinguished, not only by his reason, but by this singular passion from other animals, 
which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable 
generation of knowledge, exceeds the short vehemence of any carnal pleasure."""

encoded_test = base64_encode(test)
print(encoded_test)
>>> TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCAKd2hpY2ggaXMgYSBsdXN0IG9mIHRoZSBtaW5kLCB0aGF0IGJ5IGEgcGVyc2V2ZXJhbmNlIG9mIGRlbGlnaHQgaW4gdGhlIGNvbnRpbnVlZCBhbmQgaW5kZWZhdGlnYWJsZSAKZ2VuZXJhdGlvbiBvZiBrbm93bGVkZ2UsIGV4Y2VlZHMgdGhlIHNob3J0IHZlaGVtZW5jZSBvZiBhbnkgY2FybmFsIHBsZWFzdXJlLg==

decoded = base64_decode(encoded_test)
print(decoded)
>>> Man is distinguished, not only by his reason, but by this singular passion from other animals, 
which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable 
generation of knowledge, exceeds the short vehemence of any carnal pleasure.

```
