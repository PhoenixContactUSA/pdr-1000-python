# PDR Python Client

This module/example code implements connectivity and helper functions for the PDR 1000. In order to utilize all functionality of the module, the PDR 1000 must first be connected to successfully using the getConfig() function. The example.py shows how this should be implemented.

## getConfig

The getConfig function serves the purpose of collecting the configuration of the remote PDR 1000 and also initializes the module itself.  Without the getConfig message, the other functions will raise an exception

## getLogData

The getLogData function requests log data between two timestamps in epoch time.

```python
    now = int(time.time())
    lastMin = now - 60
    data = pdr.getLogData(lastMin,now)
```
