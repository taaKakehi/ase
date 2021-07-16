import os
import time
import ftplib

def main():

        #hostname = 'file-server1.lib.kochi-tech.ac.jp'
	#upload_src_path = '/home/pi/camera/Yoshiken.jpg'
	#upload_dst_path = '/public_html/'
	#username = 'yoshilab'
    

	os.system('sudo fswebcam -r 480x360 /home/pi/camera/ase.jpg')
	os.system('sudo scp -i ase_g4.pem /home/pi/camera/ase.jpg ec2-user@44.195.26.247:/home/ec2-user/yolov5/detect_image/')
	time.sleep(10)
	#ftp_upload(hostname, username, password, upload_src_path, upload_dst_path)
'''
def ftp_upload(hostname, username, password, upload_src_path, upload_dst_path):
	ftp = ftplib.FTP(hostname)
	ftp.set_pasv('true')
	ftp.login(username, password)
	fp = open(upload_src_path, 'rb')
	ftp.storbinary('STOR ' + upload_dst_path + 'Yoshiken.jpg',fp)
	ftp.close()
	fp.close()
'''

if __name__ == '__main__':
	main()
