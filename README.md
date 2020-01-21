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

The returned data structure is a dictionary with keys representing each io point name, and the timestamps.  The value of these keys are an array of the associated data points where each index of the timestamps array corresponds with the associated data point in the point arrays.

## getLogInfo

The log info request returns detailed information regarding the status and contents of the log information on the PDR 1000.  This function calls the api endpoint and adds some useful information to the return value.  An example return value is below:

```python
{   'fillState': 0,
    'firstDate': 1579632297000,
    'frameSize': 18,
    'indices': [   {'lI': 161, 'sI': 0, 'sR': 100, 'sU': 1579632297000},
                   {'lI': 1405907, 'sI': 162, 'sR': 100, 'sU': 1579632297900}],
    'lastDate': 1579640107600,
    'logFileSize': 1405908,
    'memoryPointer': 1405908,
    'recording': 1,
    'totalMemory': 1199999988,
    'validDates': [   {'endDate': 1579632297900, 'startDate': 1579632297000},
                      {'endDate': 1579640107600, 'startDate': 1579632297900}]}
```

The fill state value is 1 or 0 representing whether or not the memory on the device is full.  The first date is the epoch time where the first recorded data point can be found.  The frameSize value is the number of bytes stored per recording.  The indices array is data which is used to calculate the 'validDates' property.  The last date is the last recording time stamp in epoch milliseconds (UTC time).  The 'logFileSize' is the number of bytes of raw log data currently being consumed on the device.  The 'memoryPointer' is a byte pointer in the log file system to the latest recorded data point.  The 'recording' property is 1 for actively recording and 0 for stopped recording.  The 'totalMemory' property is the number of bytes available for raw recorded data.  This is the maximum value which the logFileSize can achieve.  Finally, the 'validDates' property is an array of dates in UTC time where valid log data is available.  This is calculated based on the 'indices' values. For collecting data, the UTC times which are submitted to the PDR with the getLogInfo DO NOT have to match these dates.  The PDR 1000 will automatically provide all available log data between the dates provided.  The validDates information is intended to be used for determining where recording may have been manually stopped or when the PDR may have been turned off, etc.
