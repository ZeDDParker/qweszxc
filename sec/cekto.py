global token
try:
	token = open("log.txt","r").read()
except IOError:
	os.system("rm -rf log.txt")
	print
	print tutup+"["+merah+"!"+tutup+"] Token not found"
	print tutup+"["+merah+"!"+tutup+"] You must log'in again"
	login()
