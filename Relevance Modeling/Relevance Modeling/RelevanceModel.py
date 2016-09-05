from __future__ import division
from math import log
import glob,os,time,csv
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()
stop=stopwords.words('english')
stemmer=PorterStemmer()

try:
    os.remove("Query_W1.txt")
    os.remove("Query_W2.txt")    
    os.remove("Query_W1_vector.txt")
    os.remove("Query_W2_vector.txt")
    os.remove("Doc_W2_vector.txt")
    os.remove("Doc_W2_vector.txt")
except OSError:
    pass

queries=[]
var=""

def parsed(word):
	tempstr=""
	word=word.split(" ")
	for token in word:
		if token not in stop:
		  # token=stemmer.stem(token).encode('utf-8')
		  token=lmtzr.lemmatize(token,'v').encode('utf-8')
		  token=lmtzr.lemmatize(token).encode('utf-8')
		  tempstr=tempstr+" "+token
	return tempstr


with open('hw3.queries','rb') as csvin:
	reader=csv.reader(csvin)
	for line in reader:
		if len(line)>0 and "Q" in line[0]:
			if not (not var):
				queries.append(var)
			var=""	
		if len(line)>0 and "Q" not in line[0]:
			tempstr=parsed(line[0])
			var=var+" "+tempstr

f=open('Queries.txt','w')
queries.append(var)
f.write('\n'.join(map(str,queries)))

Scores,Length,Scores1,Length1,Weight_doc=[],[],[],[],[]

doc_len = open('Doclen.txt','r')
max_tf = open('MaxTF.txt','r')
index_file=open('Index.txt')
document_file=open('Document.txt','r')
title_file=open('Title.txt','r')

doc_len_q = open('Doclen_Query.txt','r')
max_tf_q = open('MaxTF_Query.txt','r')
index_file_q=open('Index_Query.txt')


ans_1=open('Query_W1.txt','a')
ans_2=open('Query_W2.txt','a')
ans_3=open('Query_W1_vector.txt','a')
ans_4=open('Query_W2_vector.txt','a')
ans_5=open('Doc_W1_vector.txt','a')
ans_6=open('Doc_W2_vector.txt','a')

def get_values(doc_len,max_tf,index_file):
	# To get the doclen, collection size and avg document length
	doclen=[]
	avgdoclen,collectionsize=0,0

	for doc in doc_len:
		dict1=eval(doc)
		avgdoclen=avgdoclen+dict1['doclen']
		collectionsize=collectionsize+1
		doclen.append(dict1['doclen'])

	avgdoclen=avgdoclen/collectionsize

	#To get max_tf
	maxtf=[]
	for mtf in max_tf:
		dict1=eval(mtf)
		maxtf.append(dict1['max_tf'])

	#Get the json format of Index_final
	index=[]
	for element in index_file:
		dict1=eval(element)
		index.append(dict1)

	return doclen,maxtf,index,avgdoclen,collectionsize


doclen,maxtf,index,avgdoclen,collectionsize=[],[],[],0,0
doclen_q,maxtf_q,index_q,avgdoclen_q,collectionsize_q=[],[],[],0,0

doclen,maxtf,index,avgdoclen,collectionsize=get_values(doc_len,max_tf,index_file)
doclen_q,maxtf_q,index_q,avgdoclen_q,collectionsize_q=get_values(doc_len_q,max_tf_q,index_file_q)

document,title=[],[]
#To get document vector representation
for term in document_file:
	dict1=eval(term)
	document.append(dict1['text'])

for term in title_file:
	dict1=eval(term)
	title.append(dict1['title'])

def weight_compute(word,docnum,inde,flag):
	doclen1=doclen_q[docnum-1] if flag else doclen[docnum-1] 	#flag = true = query term
	avgdoclen1=avgdoclen_q if flag else avgdoclen 
	collectionsize1=collectionsize_q if flag else collectionsize
	maxtf1=maxtf_q[docnum-1] if flag else maxtf[docnum-1]
	index1=index_q[inde] if flag else index[inde]
	list_index=index1['docnum'].index((docnum))
	tf=index1['count'][list_index]
	df=index1['df']

	W1 = (0.4 + 0.6 * log (float(tf) + 0.5) / log (float(maxtf1) + 1.0)) * (log (float(collectionsize1) / float(df))/ log (float(collectionsize1)))
	W2 = (0.4 + 0.6 * (float(tf) / (float(tf) + 0.5 + 1.5 *(float(doclen1) / float(avgdoclen1)))) * log (float(collectionsize1) / float(df))/ log (float(collectionsize1)))
	return float(W1),float(W2) 	#level true will return the weight computed using W1

for i in xrange(0,collectionsize,1):
	Weight_doc.append(0)

def clear():
	del Scores[:]
	del Scores1[:]
	del Length[:]
	del Length1[:]
	# del Weight_doc[:]
	for i in range(0,collectionsize,1):
		Scores.append(0)
		Scores1.append(0)
		# Weight_doc.append(0)
		Length.append(doclen[i])
		Length1.append(doclen[i])

def cosine_score(query,docnum):
	clear()
	doclist,wtq_l,wtq1_l=[],[],[]
	ans_3.write("\n"+str(query))
	ans_4.write("\n"+str(query))
	for word in query.split(' '):
	  if not (not word) and not (not word.strip('-/\n,.\t()[] ')):
	  	word=word.strip('-/')
		post=filter(lambda person: person['term'] == word, index_q)
		wtq,wtq1=weight_compute(word,int(docnum),index_q.index(post[0]),True)
		wtq_l.append(wtq)
		wtq1_l.append(wtq1)
		post=filter(lambda person: person['term'] == word, index)
		if not(not post):
			index_post=index.index(post[0])
			for entry in index[index_post]['docnum']:
				if int(entry) not in doclist:
					doclist.append(int(entry))
				
				wtd,wtd1=weight_compute(word,int(entry),index_post,False)
				
				if Weight_doc[int(entry)-1]==0:
					Weight_doc[int(entry)-1]={'word':[word],'weight':[wtd],'weight1':[wtd1]}
				elif word not in Weight_doc[int(entry)-1]['word']:
					Weight_doc[int(entry)-1]['word'].append(word)
					Weight_doc[int(entry)-1]['weight'].append(wtd)
					Weight_doc[int(entry)-1]['weight1'].append(wtd1)

				Scores[int(entry)-1]=Scores[int(entry)-1]+(wtd*wtq)
				Scores1[int(entry)-1]=Scores1[int(entry)-1]+(wtd1*wtq1)

	ans_3.write("\n"+str(wtq_l))
	ans_4.write("\n"+str(wtq1_l))			
	for score in doclist:
		Scores[score-1]=Scores[score-1]/Length[score-1]
		Scores1[score-1]=Scores1[score-1]/Length1[score-1]
	return Scores,Scores1	


def compute_vector(query,docnum,term,level):
	doclist,wtq_l,wtq1_l=[],[],[]
	for word in query.split(' '):
	  if not (not word) and not (not word.strip('-/\n,.\t()[] ')):
	  	word=word.strip('-/')
		if word in term and word in Weight_doc[docnum]['word'] and word not in doclist:
			doclist.append(word)
			inde=Weight_doc[docnum]['word'].index(word)
			if level:
				ans_5.write("\n Word : "+str(Weight_doc[docnum]['word'][inde])+"  VectorRep:  "+str(Weight_doc[docnum]['weight'][inde]))
			else:
				ans_6.write("\n Word : "+str(Weight_doc[docnum]['word'][inde])+"  VectorRep:  "+str(Weight_doc[docnum]['weight1'][inde]))

def ranked_order(Top1,Top2,term):
	sorted_Top=Top1
	sorted_Top1=Top2
	sorted_Top=sorted(Top1,reverse=True)
	sorted_Top1=sorted(Top2,reverse=True)
	for i in range(0,5,1):
		docnum=Top1.index(sorted_Top[i])
		docnum1=Top2.index(sorted_Top1[i])
		# print str(docnum)+"  "+str(Top1[Top1.index(sorted_Top[i])])
		# print str(docnum1)+"  "+str(Top2[Top2.index(sorted_Top1[i])])
		# print Top1[499]
		# print Top2[499]
		ans_1.write("   Document No: "+str(docnum+1)+"  "+str(document[docnum])+"\n")
		ans_1.write("   Rank is: "+str(i)+" External Doc ID: "+str(docnum+1)+"\n"+" Title: "+str(title[docnum])+"\n")
		ans_5.write("\n\n Document is: "+str(document[docnum])+" \n Rank: "+str(i+1))
		ans_6.write("\n Document is: "+str(document[docnum1])+" Rank: "+str(i+1))
		compute_vector(document[docnum],docnum,term,True)				
		compute_vector(document[docnum1],docnum1,term,False)

		ans_2.write("   Document No: "+str(docnum1+1)+"  "+str(document[docnum1])+"\n")
		ans_2.write("   Rank is: "+str(i)+" External Doc ID: "+str(docnum1+1)+"\n"+" Title: "+str(title[docnum1])+"\n")

docnum=0
for term in queries:
	Top=[]
	docnum=docnum+1
	Top,Top_2=cosine_score(term.strip('/\n,.\t()[] '),docnum)
	# print Top[499]
	# print len(Top_2)
	ans_1.write("\n")
	ans_2.write("\n")
	ans_1.write("Query:"+str(docnum)+": is : "+term+"\n") 
	ans_1.write("  It's top five ranked documents are: "+"\n")
	ans_2.write("Query:"+str(docnum)+": is : "+term+"\n") 
	ans_2.write("  It's top five ranked documents are: "+"\n")
	ans_5.write("\n\n\n Query  is: "+str(docnum))
	ans_6.write("\n\n\n Query  is: "+str(docnum))
	ranked_order(Top,Top_2,term)
