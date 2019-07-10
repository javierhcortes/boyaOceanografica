from ftplib import FTP

ftp = FTP('localhost')#,'anonymous')

ftp.login(user='javier', passwd='******')

ftp.cwd('/home/javier/')
files = ftp.dir()

print (files)


def grabFile():
    fileName = 'fileName.txt'
    localfile = open(fileName, 'wb')
    ftp.retrbinary('RETR ' + fileName, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    fileName = 'fileName.txt'
    ftp.storbinary('STOR ' + fileName, open(fileName))
    ftp.quit()


# ftp.cwd('debian')               # change into "debian" directory
# ftp.retrlines('LIST')           # list directory contents
# ftp.retrbinary('RETR README', open('README', 'wb').write)
ftp.quit()

