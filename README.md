# ST-Device-with_Siri-main

Works to control on Samsung Smartthings and Apple homekits across shortcuts without any complex bridges.

A. Samsung TV smartthings access from Iphone, Macbook, or Ipad.

B. Touch to switch On/Off Samsung TV or change desired Channel.

C. Ask Siri to control Samsung TV or devices from smartthings.

Procedure and Steps:
To use these functions to control Samsung device, any command shortcuts "test device on"
and one common API shortcut "ST_Device_CMD_API".

Command shortcut will prepare JSON data and call API shortcut to post data to desired samsung device.

Before use of API shortcut, you need to edit 'pat' feild with your personal access token(ID) for the ST_Rule_API,
go to smartthings page for Authorization and Permissions provided by https://developer.smartthings.com/docs/getting-started/authorization-and-permissions


Tips for using command shortcuts:

1. After downloaded, unzip the archive and tap each Shortcut to add it to the Shortcut app where you can can edit and run the Shortcut.

2. Command shortcut contains json data like [{"component": "main","capability": "switch","command":"on"}].

3. Edit "cmdJSON" field in shortcut with more controls provided in file "ST_API.json" or running ST_Query.py.

4. You need to edit "deviceid" field in shortcut with device ID provided by https://my.smartthings.com/advanced
, and click into device page for all your devices on smartthings.

5. Use Siri to execute your Shortcuts by saying “Hey Siri Shortcut yourShortName” or “Hey Siri yourShortName”

6. Once you’ve created your Shortcuts, you can added them to your Home Screen as well as widget for execution. 

Good Luck and Enjoy!
