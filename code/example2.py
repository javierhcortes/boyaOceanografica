import os
import sys 
from ftplib import FTP

h_local_files = [] # create local dir list
h_remote_files = [] # create remote dir list

h_local = '/home/javier/boyaUdec/data/local' # local dir

#ftp = FTP('ftp.server.com')
#ftp.login('user', 'pass')

ftp = FTP('localhost')#,'anonymous')
ftp.login(user='javier', passwd='******')


if os.listdir(h_local) == []:
    print ('Directorio local vacio')
else:
    print ('construyendo lista de archivos locales...\n')
    for file_name in os.listdir(h_local):
        h_local_files.append(file_name) # populate local dir list

# Comprobar la existencia de este dir
ftp.sendcmd('CWD /home/javier/boyaUdec/data/remoto')
print ('Construyendo lista de archivos remotos...\n')
for rfile in ftp.nlst():
    # aqui se debe rellenar con condiciones para filtrar archivos (*.roi, *.adc y *.hdr)
    #if rfile.endswith('.jpg'): # i need only .jpg files
    h_remote_files.append(rfile) # populate remote dir list

h_diff = sorted(list(set(h_remote_files) - set(h_local_files))) # difference between two lists

for h in h_diff:
    with open(os.path.join(h_local,h), 'wb') as ftpfile:
        #s = ftp.retrbinary('RETR ' + h, ftpfile.write) # retrieve file
        s = ftp.retrbinary('RETR ' + h, lambda s: ftpfile.write(s) and sys.stdout.write('.'))
        print ('Cargando archivos', h)
        if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
            print ('OK\n') # print 'OK' if transfer was successful
        else:
            print (s) # if error, print retrbinary's return