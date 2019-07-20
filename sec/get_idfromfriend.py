try:
	os.mkdir('out')
except OSError: pass
print
idt = raw_input(tutup+"["+lime+"+"+tutup+"] Input ID friend : "+lime)
try:
	a = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
	f = json.loads(a.text)
	print tutup+"["+lime+"+"+tutup+"] Get id from : "+lime+f['name']
except KeyError:
	print tutup+"["+merah+"!"+tutup+"] Not Found"
	raw_input(tutup+"\nBack ...")
	menu_dump()
r = requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+token)
z = json.loads(r.text)
print tutup+"["+lime+"+"+tutup+"] Fetching id all friend from "+lime+f['name']+tutup
print tutup+"["+lime+"+"+tutup+"] Start ..."
save = open('out/idfriendfromfriend.txt','w')
for y in z['friends']['data']:
	idfromfriend.append(y['id'])
	save.write(y['id']+'\n')
	print (tutup+"\r["+lime+"+"+tutup+"] Total : "+lime+str(len(idfromfriend))),;sys.stdout.flush();time.sleep(0.0001)
save.close()
print tutup+"\n["+lime+"+"+tutup+"] Successfully get id friend from "+lime+f['name']+tutup
done = raw_input(tutup+"["+lime+"+"+tutup+"] Save file with name : "+lime)
os.rename('out/idfriendfromfriend.txt','out/'+done)
print tutup+"["+lime+"+"+tutup+"] File saved : "+lime+"out/"+done+tutup
print tutup+"["+lime+"+"+tutup+"] Done"
raw_input(tutup+"\nBack ...")
menu()
