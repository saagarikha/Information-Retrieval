The folder contains :
	Folder Version1:
	Index_Creation1.py 		- Creating the dictionary,posting and the index files for Cranfield Dataset
	Index_Sorting1.py 		- Computing the gaps between the Document ID's in the index
	Compression1.py			- Compressing the files based upon gamma encoding and block size compression
	Answer.py			- Answers obtained for the question asked
	Answers1.txt			- Answers for questions in part 1 assignment (WILL BE GENERATED)
	Dictionary.txt			- Dictionary file for in part 1 assignment (contains term, TotFreq, Ndocs, term_length)						      (WILL BE GENERATED)
	Compress_Dictionary.txt		- Dictionary file for in part 1 assignment (contains term, TotFreq, Ndocs, term_length, term_pointer)				      (WILL BE GENERATED)
	Postings.txt			- Posting file for part 1 assignment (contains Doc#, term, Freq#,max_tf,doclen)							      (WILL BE GENERATED)
	Compression_Postings.txt	- Posting file for part 1 assignment (contains encode(Doc#), term, encode(Freq#),encode(max_Tf),encode(doclen))			      (WILL BE GENERATED)
	Index.txt			- Final output file for part 1 assignment (contains an array of count list,term, document list,df,tf)				      (WILL BE GENERATED)
	Compression_Index.txt		- Final output file for part 1 assignment (contains an array of encode(count list),term, encpde(document list),encode(tf),encode(df)) (WILL BE GENERATED)
					For ex:[count#doc<l>,count#doc<k>....],term:<Term>,[#doc<l>,#doc<k>..]
	MaxTF.txt			- Document ID and its maximum term frequency in the collection
	Doclen.txt			- Document ID and its document length in the collection

How to run the program:
	Dependencies:	NLTK to be downloaded.
		How to download:
			1. Install pip : python get-pip.py
				or upgrade it as: pip install -U pip (Linux)
			2. Install nltk as: sudo pip install -U nltk
			3. Test installation as: 
				Run the python interpreter: python (in terminal)
				Type :	import nltk
				Then install nltk as : nltk.download('all')
			4. Ensure it is the latest version: pip install --upgrade nltk (in the terminal, not python interpreter)

TO RUN THE PROGRAM AFTER INSTALLING DEPENDENCIES:
	UNZIP THE FILE AND SAVE IT IN DESIRED LOCATION.
	GOTO THE SPECIFIC LOCATION AND ALSO HAVE THE Cranfield FOLDER IN THE LOCATION WHERE THE UNZIPPED FILE IS LOCATED.
	NOTE: SAVE THE COLLECTION INSIDE A FOLDER Cranfield (The entire 1400 files should be inside a folder named Cranfield)
	python Index_Creation1.py (It takes sometime, but the output will be saved in different files as: Answers_part1.txt, Postings_part1.txt, output_part1.txt, Dictionary_part1.txt)
	python Index_Sorting1.py	  (Generates Gaps between the Doc ID's in doc list of index file)
	python Compression1.py	  (Generates the compressed versions of Dictionary, Postings and Index file based on gamma encoding and block size compression)
	python Answer.py	  (Generates the Answer1.txt file)

How I assumed the program:
	1. I removed the stopwords in both the part 1 and part 2.
	2. In part 2 I removed the stemmed words also.
	3. I did not consider digits as the input file.
	4. The SGML tags, only the content in the <TEXT> and </TEXT> is taken.
	4. The document number in <DOCNO> is taken into consideration for the document number.
	5. The words hypenated are taken as a single word and hypens are included to ensure the meaning.
	6. The tokenization for part 1 and 2 are not case sensitive.
	7. The Possessives are removed and made into as a single word. Ex: sheriff's is made as sheriff
	8. The acronyms are taken as acronyms and included in the tokenization.

Algorithms and Data Structures used:
	- I assumed a list of dictionary to save the tokenized documents.
	- The dictionary contains the output as :
		Postings file : Contains the Document number, Frequency of the word and the word.
			Ex: {'term': <Term>, 'Doc#':<DocNO>, 'Freq': <count of word in document>}
		Dictionary file:Contains the term, TotalFrequency and NumberofDocs.
			Ex: {'term': <Term>, 'TotFreq': <Total frequency of word in the entire collection>, 'NDocs': <Number of documents in which the term is present in the complete collection>}
		Index file    : Contains the complete output of the tokenization.
			Ex: {'term':<Tokenized term>,'count': [#countIndoc<l>,#countInDoc<k>...],'DocNo':[#DocNo<l>,#DocNo<k>...]}
				Note: (count and docno have the same length of list)
		Answers file   : Contains the answer for the question asked in Homework 2  
