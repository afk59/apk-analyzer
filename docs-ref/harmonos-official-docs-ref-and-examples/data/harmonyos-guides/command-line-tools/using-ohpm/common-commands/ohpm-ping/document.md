# ohpm ping

Pings the address of the ohpm repository.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm ping

#### Description

This command is used to ping a given or configured repository address. If the address is valid, related information is displayed as follows:

ohpm INFO: PING your\_registry
ohpm INFO: PONG 255ms

Otherwise, error information is displayed as follows:

ohpm INFO: PING your\_registry
ohpm ERROR: HttpCode 404, API ping in your\_registry - Not Found

#### Options

## registry

-   Default value: ""
-   Type: URL

You can configure the **\--registry <registry>** parameter at the end of the **ohpm ping** command to specify a repository address. If the parameter is not specified, the repository address is obtained from the configuration by default.

## fetch\_timeout

-   Default value: 60000
-   Type: number
-   Alias: ft

You can configure the **\--ft <number>** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm ping** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm ping** command to enable HTTPS certificate verification or configure **\--strict\_ssl false** to disable it.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm ping** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.
