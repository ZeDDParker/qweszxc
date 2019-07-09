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
