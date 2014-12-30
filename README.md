Project Statistical Models of the Emotionality of Speech and Written Text (2011-2014) was supported by the National Programme for Estonian Language Technology (2011-2017) of the Estonian Ministry of Education and Research.


This is a program classifying an Estonian text as positive, neutral or negative.
It is running on server http://peeter.eki.ee:5000/valence 

It is optimized for server environment but can be run also as a standalone program:
```
  python valencecolor.py textfile.txt
```
This will produce a file `textfile.txt.html` where all emotionally relevant word are marked with CSS style. The limitation is that it does not print out the summary information. As a prerequisite the [NLTK](http://www.nltk.org) must be installed on the computer.


### Files

 - korpus.csv - corpus for training the NLTK model
 - sqnad.csv - dictionary of Estonian words 
 - bayes.py - [NLTK](http://www.nltk.org) wrapper
 - valencecolor.py - main program
 - colored.mak - a html template example.

