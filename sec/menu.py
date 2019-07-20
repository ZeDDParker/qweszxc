global id,token
try:
	token = open("log.txt","r").read()
except IOError:
	os.system("reset")
	print merah+" ||  || "+merah+"  ╔╦╗"+tutup+"┌─┐┬─┐┬┌─   "+merah+"╔═╗╔╗"+tutup
	print merah+" \\\\"+putih+"()"+merah+"//"+merah+"    ║║"+tutup+"├─┤├┬┘├┴┐───"+merah+"╠╣ ╠╩╗"+tutup
	print merah+"//"+putih+"(__)"+merah+"\\\\"+merah+"  ═╩╝"+tutup+"┴ ┴┴└─┴ ┴   "+merah+"╚  ╚═╝"+kuning+"v1.8"+tutup
	print merah+"||    || "+tutup+u" \u001b[7m Author: ZeDD Parker \u001b[0m"
	print
	choose_banner()
try:
	cek  = requests.get("https://graph.facebook.com/me?access_token="+token)
	a    = json.loads(cek.text)
	nama = a['name']
	id   = a['id']
except KeyError:
	print tutup+"["+kuning+"+"+tutup+"] Checkpoint"
	os.system("rm -rf log.txt")
	keluar()
except requests.exceptions.ConnectionError:
	exit(merah+"[!] No Connection")
os.system("reset")
print merah+" ||  || "+merah+"  ╔╦╗"+tutup+"┌─┐┬─┐┬┌─   "+merah+"╔═╗╔╗"+tutup
print merah+" \\\\"+putih+"()"+merah+"//"+merah+"    ║║"+tutup+"├─┤├┬┘├┴┐───"+merah+"╠╣ ╠╩╗"+tutup
print merah+"//"+putih+"(__)"+merah+"\\\\"+merah+"  ═╩╝"+tutup+"┴ ┴┴└─┴ ┴   "+merah+"╚  ╚═╝"+kuning+"v1.8"+tutup
print merah+"||    || "+tutup+u" \u001b[7m Author: ZeDD Parker \u001b[0m"
print
print tutup+"        ["+blue+"●"+tutup+"] User : "+lime+nama+tutup
print
choose_banner()
