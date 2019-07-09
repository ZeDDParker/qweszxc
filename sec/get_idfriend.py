try:
	os.mkdir('out')
except OSError:
	pass
print
r = requests.get("https://graph.facebook.com/me/friends?access_token="+token)
z = json.loads(r.text)
print tutup+"["+lime+"+"+tutup+"] Fetching id all friend"+tutup
print tutup+"["+lime+"+"+tutup+"] Start ..."
save = open('out/idfriend.txt','w')
for y in z['data']:
	idfriend.append(y['id'])
	save.write(y['id']+'\n')
	print (tutup+"\r["+lime+"+"+tutup+"] Total : "+lime+str(len(idfriend))),;sys.stdout.flush();time.sleep(0.0001)
save.close()
print tutup+"\n["+lime+"+"+tutup+"] Successfully get id friend"
done = raw_input(tutup+"["+lime+"+"+tutup+"] Save file with name : "+lime)
os.rename('out/idfriend.txt','out/'+done)
print tutup+"["+lime+"+"+tutup+"] File saved : "+lime+"out/"+done+tutup
print tutup+"["+lime+"+"+tutup+"] Done"
raw_input(tutup+"\nBack ...")
menu()
