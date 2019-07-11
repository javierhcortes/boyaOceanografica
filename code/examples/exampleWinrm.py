import winrm

host = 'YourWindowsHost'
domain = 'YourDomain'
user = 'YourDomainUser'
password = 'YourPassword'

session = winrm.Session(host, auth=('{}@{}'.format(user,domain), password), transport='ntlm')

result = session.run_cmd('ipconfig', ['/all']) # To run command in cmd

result = session.run_ps('Get-Acl') # To run Powershell block