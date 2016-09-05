f=open('Index.txt','r')
f1=open('Index_Final.txt','w')

var=[]

for item in f:
	dict1=eval(item)
	dict1['docnum'],dict1['count'] = zip(*sorted(zip(dict1['docnum'], dict1['count'])))
	dict1['docnum']=list(dict1['docnum']) 
	dict1['count']=list(dict1['count'])
	index=0
	for val in dict1['docnum']:
		if index>0:
			dif=val-dict1['docnum'][index-1]
			dict1['docnum'][index]=dif
		index=index+1	
	var.append(dict1)

f1.write('\n'.join(map(str,var)))	
f1.close()
