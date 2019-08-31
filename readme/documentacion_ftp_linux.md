# pasos para instalar un servidor ftp

en ubuntu instalar vsftpd (very secure FTP daemon) package.

    sudo apt install vsftpd ftp


# configurando un servidor linux con ftp

We will edit /etc/vsftpd/vsftpd.conf you can do this with gedit (If installed) or vi command.

    anonymous_enable=YES  ##   permit any one to access FTP server with authentication.

# Uncomment the following line

    local_enable=YES        ##                            allow users in /etc/passwd to login
    write_enable=YES          ##                   allow users to write files. “NO” will permit only to read.


# Instalacion y manejo de FTP en windows

https://www.solvetic.com/tutoriales/article/5695-como-instalar-configurar-servidor-ftp-windows-10/

https://www.windowscentral.com/how-set-and-manage-ftp-server-windows-10
