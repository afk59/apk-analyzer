# How do I select a crash collection mode? What are the differences between ErrorManager, FaultLog, and HiAppEvent in terms of crash listening?

HiAppEvent is recommended.

| 
Mode

 | 

Scope

 | 

Trigger Mode

 | 

Scenes

 | 

Crash Symptom

 |
| :-- | :-- | :-- | :-- | :-- |
| 

ErrorManager

 | 

js crash

 | 

The caller proactively queries the fault data of the current process and reports at most 10 pieces of information (The obtained data is a subset of the data returned by FaultLog and is listened by FaultLog).

 | 

Notifies an error.

 | 

An error is thrown, and the process does not exit.

 |
| 

FaultLog

 | 

js crash, cpp crash, app freeze

 | 

Observer mode. A listener is registered first, and a callback is invoked to return the result.

 | 

Queries recent fault logs.

 | 

An error log is generated, and the process does not exit.

 |
| 

HiAppEvent

 | 

js crash, cpp crash, app freeze

 | 

Observer mode. A listener is registered first, and a callback is invoked to return the result.

 | 

Records and listens for events, including behavior, fault, statistic, and security events.

 | 

The process exits, and the crash information is processed when the application is accessed again.

 |
