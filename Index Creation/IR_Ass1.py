from __future__ import division
import glob,os
from nltk.stem.porter import *
from nltk.corpus import stopwords
path = 'Cranfield'

var,tmp=[],[]
docnum=0
flag,ff,unique=1,0,0
op=open('output_part1.txt','w')
op1=open('Dictionary_part1.txt','w')
op2=open('Postings_part1.txt','w')
op3=open('Answers_part1.txt','w')
stop=stopwords.words('english')
stemmer=PorterStemmer()

for filename in glob.glob(os.path.join(path, '*')):
	docnum=docnum+1
	f=open(filename,'r')
	for item in f:
		if "<DOCNO>" in item:
			ff=1
		if ff==1 and "<DOCNO>" not in item:
			docnum=int(item)
			ff=0
		if "<" in item and "<TEXT>" not in item:
			flag=1
	  	if "<TEXT>" in item:
	  		flag=0
		if "<" not in item and flag==0:
			for line in item.strip('/\n,.\t()[] ').split(' '):
				if line not in stop and not line.isdigit():
					#line=stemmer.stem(line).encode('utf-8')
					line=line.strip("=()/ \n\t,.[]-\\*+'\"")
					if line and not filter(str.isdigit,line).isdigit() and line not in stop: 
						k=filter(lambda person: person['term'] == line, var)
						if  filter(lambda person: person['term'] == line, var):
							if k[0]['docnum'][-1]==docnum:
								k[0]['count'][-1]=k[0]['count'][-1]+1
							else:	
								k[0]['docnum'].append(docnum)
								k[0]['count'].append(1)
						else:
							var.append({'term':line,'count':[1],'docnum':[docnum]})
							
	f.close()
dictionary,postings,temp=[],[],[]
var=sorted(var,key=lambda k:k['term'])
tmp=sorted(var,key=lambda k:len(k['docnum']),reverse=True)
for i in range(0,31,1):
	temp.append(tmp[i])
temp=sorted(temp,key=lambda k:k['term'])

for val in var:
	ndocs=len(val['docnum'])
	for i in range(0,len(val['docnum']),1):
		postings.append({'Term':val['term'],'Doc#':val['docnum'][i],'Freq':val['count'][i]})
	totfreq=sum(cnt for cnt in val['count'])
	if totfreq==1: unique+=1
	dictionary.append({'term':val['term'],'Ndocs':ndocs,'TotFreq':totfreq})

ans=[]

ans.append("Tokens in cranfield text collection")
ans.append(len(postings))
ans.append("Number of unique words in cranfield text")
ans.append(len(dictionary))
ans.append("Count of words occuring only once")
ans.append(unique)
ans.append("Top 30 files and their information")
for i in range(0,len(temp),1): ans.append(temp[i])
ans.append("Average word tokens")
ans.append(len(postings)/1400)


op3.write('\n'.join(map(str,ans)))	
op3.close()

op1.write('\n'.join(map(str,dictionary)))	
op1.close()

op2.write('\n'.join(map(str,postings)))	
op2.close()

op.write('\n'.join(map(str,var)))	
op.close()
