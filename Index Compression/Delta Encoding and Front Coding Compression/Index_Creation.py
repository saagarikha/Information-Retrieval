from __future__ import division
import glob,os,time
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


lmtzr = WordNetLemmatizer()
path = 'Cranfield'

var,tmp,max_tf,doclen=[],[],[],[]
docnum=0
flag,ff,unique,doc,line_cnt=1,0,0,0,0
op=open('Index.txt','w')
op1=open('Dictionary.txt','w')
op2=open('Postings.txt','w')
op3=open('Answers.txt','w')
op4=open('Doclen.txt','w')
op5=open('MaxTF.txt','w')
op6=open("Answers2.txt","w")

stop=stopwords.words('english')
stemmer=PorterStemmer()

def clean(line):
	line=line.replace("=","")
	line=line.replace("(","")
	line=line.replace(")","")
	line=line.replace("/","")
	line=line.replace(" ","")
	line=line.replace("\\","")
	line=line.replace("\n","")
	line=line.replace("\t","")
	line=line.replace(",","")
	line=line.replace(".","")
	line=line.replace("[","")
	line=line.replace("]","")
	if line and "-" in line[0]:
		line=line.replace("-","")
	line=line.replace("*","")
	line=line.replace("+","")
	line=line.replace("\'","")
	line=line.replace("\"","")
	return line

start=time.clock()

for filename in glob.glob(os.path.join(path, '*')):
	docnum=docnum+1
	f=open(filename,'r')
	for item in f:
		if "<DOCNO>" in item:
			ff=1
		if ff==1 and "<DOCNO>" not in item:
			docnum=int(item)
			doc=0
			line_cnt=0
			ff=0
		if "<" in item and "<TEXT>" not in item:
			flag=1
	  	if "<TEXT>" in item:
	  		flag=0
	  	if "</TEXT>" in item:
	  		doclen[-1]['doclen']=line_cnt
	  		var[-1]['doclen']=line_cnt
		if "<" not in item and flag==0:
			for line in item.strip('/\n,.\t()[] ').split(' '):
				line_cnt=line_cnt+1
				if doc==0:
					doclen.append({'docnum':docnum,'doclen':0})
					max_tf.append({'docnum':docnum,'max_tf':0})
					doc=1
				if line not in stop and not line.isdigit():
					line=lmtzr.lemmatize(line).encode('utf-8')
					line=stemmer.stem(line).encode('utf-8')
					line=clean(line)
					if line and not filter(str.isdigit,line).isdigit() and line not in stop and len(line)>2: 
						k=filter(lambda person: person['term'] == line, var)
						if  filter(lambda person: person['term'] == line, var):
							if k[0]['docnum'][-1]==docnum:
								k[0]['count'][-1]=k[0]['count'][-1]+1
								if max_tf[-1]['max_tf']<k[0]['count'][-1]:
									max_tf[-1]['max_tf']=k[0]['count'][-1]
							else:	
								k[0]['docnum'].append(docnum)
								k[0]['count'].append(1)
						else:
							var.append({'term':line,'count':[1],'docnum':[docnum]})
							if max_tf[-1]['max_tf']==0:
									max_tf[-1]['max_tf']=1
	f.close()
dictionary,postings,temp=[],[],[]
var=sorted(var,key=lambda k:k['term'].upper())

doclen=sorted(doclen,key=lambda k:k['docnum'])
max_tf=sorted(max_tf,key=lambda k:k['docnum'])

tmp=sorted(var,key=lambda k:len(k['docnum']),reverse=True)
for i in range(0,31,1):
	temp.append(tmp[i])
temp=sorted(temp,key=lambda k:k['term'])

inde=0
for val in var:
	ndocs=len(val['docnum'])
	for i in range(0,len(val['docnum']),1):
		postings.append({'Term':val['term'],'Doc#':val['docnum'][i],'Freq':val['count'][i],'doclen':doclen[val['docnum'][i]-1]['doclen'],'max_tf':max_tf[val['docnum'][i]-1]['max_tf']})
	totfreq=sum(cnt for cnt in val['count'])
	if totfreq==1: unique+=1
	dictionary.append({'term':val['term'],'Ndocs':ndocs,'TotFreq':totfreq,'term_length':len(val['term'])})
	var[inde].update({'df':ndocs ,'tf':totfreq})
	inde=inde+1

ans=[]

mins=(time.clock()-start)/60
sec=start=(time.clock()-start)%60

op6.write("\n The time taken for the Index to be created is:"+str(int(mins))+" mins and "+str(int(sec))+" seconds ")
op6.close()

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


op5.write('\n'.join(map(str,max_tf)))	
op5.close()

op4.write('\n'.join(map(str,doclen)))	
op4.close()

op3.write('\n'.join(map(str,ans)))	
op3.close()

op1.write('\n'.join(map(str,dictionary)))	
op1.close()

op2.write('\n'.join(map(str,postings)))	
op2.close()

op.write('\n'.join(map(str,var)))	
op.close()
