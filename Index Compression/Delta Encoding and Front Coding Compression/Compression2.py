from nltk.corpus import stopwords
from nltk.stem.porter import *
import math

stemmer=PorterStemmer()

def GammaEncoding(X):
       	if X>0:
	        N1= int(math.log(float(X),2))
	        gamma=""
	        for i in range(0,N1,1): 
	        	gamma=gamma+"1"
	        gamma=gamma+"0";
	        gamma=gamma+bin(int(X)).encode('ascii')[3:]
	        gamma=int(gamma)
	        return gamma
        else:
         gamma=0
         return gamma    

def DeltaEncoding(X):
	if X>0:
		N1=int(math.log(float(X),2))
		delta=""
		delta=GammaEncoding(N1+1)
		delta=str(delta)+bin(int(X)).encode('ascii')[3:]
		return int(delta)
	else:
		delta=0
		return int(delta)

fdic=open('Dictionary.txt','r')
odic=open('Compress_Dictionary.txt','w')
f=open('Index_Final.txt','r')
f2=open('Postings.txt','r')
f3=open('Compress_Postings.txt','w')
f1=open('Compress_Index.txt','wb')

var=[]

k,cnt,flag,flag1,wc=8,0,0,0,0
temp_str=""
for item in fdic:
	dict1=eval(item)
	if flag==0 and flag1==0:
		temp_str=dict1['term'].split("-")[0]
		temp_str=stemmer.stem(temp_str).encode('utf-8')
		if flag1==0: flag1=2

	if cnt%k ==0:
		if cnt>0:
			dict1.update({'term_ptr':var[cnt-k]['term_length']})
			flag=0
		else:
			dict1.update({'term_ptr':dict1['term_length']})
			flag=0
		var.append(dict1)
	else:
		var.append(dict1)
		if temp_str in var[cnt]['term'] and flag1!=2:
			if flag==0:
				flag=1
				wc=wc+1
				var[cnt-1]['term_length']=str(len(temp_str))+temp_str+"*"+var[cnt-1]['term'].replace(temp_str,"")+str(wc)
				wc=wc+1
				var[cnt]['term_length']="*"+var[cnt]['term'].replace(temp_str,"")+str(wc)
			else:
				wc=wc+1
				var[cnt]['term_length']="*"+var[cnt]['term'].replace(temp_str,"")+str(wc)
		else:
			if temp_str not in var[cnt]['term']: 
				wc=0
				temp_str=stemmer.stem(var[cnt]['term'].split("-")[0]).encode('utf-8')
			flag1=1
			flag=0	
	cnt=cnt+1
odic.write('\n'.join(map(str,var)))
odic.close()

var=[]
for item in f:
	dict1=eval(item)
	dict1['docnum'].sort()
	index=0
	for val in dict1['docnum']:
		dict1['docnum'][index]=DeltaEncoding(val)					#gaps between the documents
		dict1['count'][index]=DeltaEncoding(dict1['count'][index])  # the term frequency in every document
		index=index+1	
	dict1['df']=DeltaEncoding(dict1['df'])							# Document Frequency
	dict1['tf']=DeltaEncoding(dict1['tf'])							# Term Frequency
	var.append(dict1)
f1.write('\n'.join(map(str,var)))
f1.close()

var=[]

for item in f2:
	dict1=eval(item)
	dict1['max_tf']=DeltaEncoding(dict1['max_tf'])
	dict1['Doc#']=DeltaEncoding(dict1['Doc#'])
	dict1['Freq']=DeltaEncoding(dict1['Freq'])
	dict1['doclen']=DeltaEncoding(dict1['doclen'])
	var.append(dict1)
f3.write('\n'.join(map(str,var)))
f3.close()
