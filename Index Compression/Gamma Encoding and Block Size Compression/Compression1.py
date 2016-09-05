import math
import sys
def GammaEncoding(X):
        if X>0:
	        N1= int(math.log(X,2))
	        gamma=""
	        for i in range(0,N1,1): 
	        	gamma=gamma+"1"
	        gamma=gamma+"0";
	        gamma=gamma+bin(X).encode('ascii')[3:]
	        return int(gamma)
        else:
         gamma=0
         return gamma    

fdic=open('Dictionary.txt','r')
odic=open('Compress_Dictionary.txt','w')
f=open('Index_Final.txt','r')
f2=open('Postings.txt','r')
f3=open('Compress_Postings.txt','w')
f1=open('Compress_Index.txt','w')

var=[]

k,cnt=8,0
for item in fdic:
	dict1=eval(item)
	if cnt%k ==0:
		if cnt>0:
			dict1.update({'term_ptr':var[cnt-k]['term_length']})
		else:
			dict1.update({'term_ptr':dict1['term_length']})
	cnt=cnt+1
	var.append(dict1)
odic.write('\n'.join(map(str,var)))
odic.close()

var=[]
for item in f:
	dict1=eval(item)
	dict1['docnum'].sort()
	index=0
	for val in dict1['docnum']:
		dict1['docnum'][index]=GammaEncoding(val)					#gaps between the documents
		dict1['count'][index]=GammaEncoding(dict1['count'][index])  # the term frequency in every document
		index=index+1	
	dict1['df']=GammaEncoding(dict1['df'])							# Document Frequency
	dict1['tf']=GammaEncoding(dict1['tf'])							# Term Frequency
	var.append(dict1)
f1.write('\n'.join(map(str,var)))
f1.close()

var=[]

for item in f2:
	dict1=eval(item)
	dict1['max_tf']=GammaEncoding(dict1['max_tf'])
	dict1['Doc#']=GammaEncoding(dict1['Doc#'])
	dict1['Freq']=GammaEncoding(dict1['Freq'])
	dict1['doclen']=GammaEncoding(dict1['doclen'])
	var.append(dict1)
f3.write('\n'.join(map(str,var)))
f3.close()
