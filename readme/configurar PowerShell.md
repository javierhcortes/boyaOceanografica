# How to Run PowerShell Commands on Remote Computers

1) Enable PowerShell Remoting on the PC You Want to Access Remotely

In Windows 10, press Windows+X and then choose PowerShell (Admin) from the Power User menu.
In Windows 7 or 8, hit Start, and then type “powershell.” Right-click the result and choose “Run as administrator.”

type the following cmdlet
    Enable-PSRemoting -Force

2)Select type of connection
For PowerShell Remoting to work in a workgroup environment, you must configure your network as a private, not public, network.

3)Configure the TrustedHosts
Configure both the PC to which you want to connect and the PC (or PCs) you want to connect from, as Administrator

    Set-Item wsman:\localhost\client\trustedhosts *

Restart WinRm

    Restart-Service WinRM

4)Test the Connection
In local computer Replace "COMPUTER" with name or ip address

    Test-WsMan COMPUTER

5)Execute a Single Remote Command

    Invoke-Command -ComputerName COMPUTER -ScriptBlock { COMMAND } -credential USERNAME

example

    Invoke-Command -ComputerName 10.0.0.22 -ScriptBlock { Get-ChildItem C:\ } -credential wjgle

6)Start a Remote Session

    Enter-PSSession -ComputerName COMPUTER -Credential USER