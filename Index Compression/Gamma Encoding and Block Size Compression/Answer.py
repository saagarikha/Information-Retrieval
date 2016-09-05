import os
from nltk.stem.porter import *
from nltk.stem.wordnet import WordNetLemmatizer

index_comp=os.path.getsize("Index_Final.txt")
index=os.path.getsize("Compress_Index.txt")
lmtzr = WordNetLemmatizer()
stemmer=PorterStemmer()

op4=open("Answers1.txt",'a')

op4.write("\n\nSize of the uncompressed Version 1:"+str(index)+" bytes")
op4.write("\n\nSize of the compressed Version 1:"+str(index_comp)+" bytes")


f=open("Index.txt",'r')
count=0


var=[]

for item in f:
	count=count+1
	dict1=eval(item)
	if dict1['term'].lower()==lmtzr.lemmatize("Reynolds").encode('utf-8').lower() or dict1['term'].lower()==lmtzr.lemmatize("NASA").encode('utf-8').lower() or dict1['term'].lower()==lmtzr.lemmatize("Prandtl").encode('utf-8').lower() or dict1['term'].lower()==lmtzr.lemmatize("flow").encode('utf-8').lower() or dict1['term'].lower()==lmtzr.lemmatize("pressure").encode('utf-8').lower() or dict1['term'].lower()==lmtzr.lemmatize("boundary").encode('utf-8').lower() or dict1['term'].lower()==lmtzr.lemmatize("shock").encode('utf-8').lower():
		var.append(dict1)

var1=[]
var2=[]
var3=[]
flag=0

f2=open("Postings.txt")
for item in f2:
	dict1=eval(item)
	if flag==0: 
		var3.append(dict1)
		var3.append(dict1)
		flag=1
	if dict1['Term'].lower()==lmtzr.lemmatize("NASA").encode('utf-8').lower():
		var1.append(dict1)
	if dict1['Freq']==dict1['max_tf']:
		var2.append(dict1)
	elif dict1['Freq']==1:
		var2.append(dict1)
	if var3[0]['max_tf']<dict1['max_tf']:
		var3[0]=dict1	
	if var3[1]['doclen']<dict1['doclen']:
		var3[1]=dict1	

var2=sorted(var2,key=lambda k:k['Doc#'])

op4.write("\n\nthe df, tf, and inverted list length (in bytes) for the terms\n\n")
op4.write('\n'.join(map(str,var)))

op4.write("\n\n the df, for NASA as well as the tf, the doclen and the max_tf, for the first 3 entries in its posting list. \n\n")
var1=sorted(var1,key=lambda k:k['Doc#'])
temp=[]
i=0
for val in var1:
	if i>=3:
		break
	else:
		temp.append({'Term':val['Term'],'Docnum':val['Doc#'],'Freq':val['Freq'],'Doclen':val['doclen'],'max_tf':val['max_tf']})	
	i=i+1
op4.write('\n'.join(map(str,temp)))

op4.write("\n\n the stem from index 2 with the largest df and the dictionary term with the lowest df\n\n ")
temp=[]
for val in var2:
	temp.append({'Term':val['Term'],'Docnum':val['Doc#'],'Freq':val['Freq']})
op4.write('\n'.join(map(str,temp)))

op4.write("\n\n the document with the largest max_tf in collection and the document with the largest doclen in the collection\n\n")
temp=[]
for val in var3:
	temp.append({'Docnum':val['Doc#'],'max_tf':val['max_tf'],'doclen':val['doclen']})
op4.write('\n'.join(map(str,temp)))
op4.close()
