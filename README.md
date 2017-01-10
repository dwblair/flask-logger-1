# flask-logger

to install:

```
pip install setuptools
pip install flask
```

to run:
```
python logger.py
```

This will set up the server at: http://127.0.0.1:5000/

You will need a public key and a private key.

As of now, these values are hard-coded into logger.py.


You can log an arbitray set of key-value pairs via a GET command, with the appropriate publickey and private key (as set in logger.py).

The values are sorted alphabetically according to their key name, then appended to a file whose name corresponds to the public key.

For example, try:
 
```
http://localhost:5000/log?publickey=222&privatekey=333&temp=32.&humidity=22.
```


