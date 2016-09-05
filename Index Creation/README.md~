The folder contains :
	IR_Ass1.py 		- Part 1 of the program description
	IR_Ass_Part2.py 	- Part 2 of the program description
	Answers.txt		- Answers for questions in part 2 assignment (WILL BE GENERATED)
	Answers_part1.txt	- Answers for questions in part 1 assignment (WILL BE GENERATED)
	Dictionary.txt		- Dictionary file for in part 2 assignment (contains term, TotFreq, Ndocs)	(WILL BE GENERATED)
	Dictionary_part1.txt	- Dictionary file for in part 1 assignment (contains term, TotFreq, Ndocs)	(WILL BE GENERATED)
	Postings.txt		- Posting file for part 2 assignment (contains Doc#, term, Freq#)		(WILL BE GENERATED)
	Postings_part1.txt	- Posting file for part 1 assignment (contains Doc#, term, Freq#)		(WILL BE GENERATED)
	output.txt		- Final output file for part 2 assignment (contains an array of count list,term, document list)	(WILL BE GENERATED)
	output_part1.txt	- Final output file for part 1 assignment (contains an array of count list,term, document list) (WILL BE GENERATED)
					For ex:[count#doc<l>,count#doc<k>....],term:<Term>,[#doc<l>,#doc<k>..]

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
	python IR_Ass1.py 	(It takes sometime, but the output will be saved in different files as: Answers_part1.txt, Postings_part1.txt, output_part1.txt, Dictionary_part1.txt)
	python IR_Ass_Part2.py 	(It takes sometime, but the output will be saved in different files as: Answers.txt, Postings.txt, output.txt, Dictionary.txt)


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
		output file    : Contains the complete output of the tokenization.
			Ex: {'term':<Tokenized term>,'count': [#countIndoc<l>,#countInDoc<k>...],'DocNo':[#DocNo<l>,#DocNo<k>...]}
				Note: (count and docno have the same length of list)
		Answers file   : Contains the answer for the question asked in Homework 1   
