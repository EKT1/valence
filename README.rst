Project Statistical Models of the Emotionality of Speech and Written Text (2011-2014) was supported by the National Programme for Estonian Language Technology (2011-2017) of the Estonian Ministry of Education and Research.


This is a program classifying an Estonian text as positive, neutral or negative.
It is running on server http://peeter.eki.ee:5000/valence 

This code is optimized for server environment but can be run also as a standalone program::

  python valencecolor.py textfile.txt

This will produce a file `textfile.txt.html` where all emotionally relevant word are marked with CSS style. The limitation is that it does not print out the summary information. As a prerequisite the `NLTK <http://www.nltk.org>`_ must be installed on the computer.


Files:

 - valence/korpus.csv - corpus for training the NLTK model
 - valence/sqnad.csv - dictionary of Estonian words 
 - valence/bayes.py - NLTK wrapper
 - valence/valencecolor.py - main program

If you use the corpora **valence/korpus.csv, valence/sqnad.csv** in your work, please cite the following paper:

  Pajupuu, Hille; Altrov, Rene; Pajupuu, Jaan (2016). Identifying polarity in different text types. *Folklore. Electronic Journal of Folklore*, 64, 25−42. `DOI <http://dx.doi.org/10.7592/FEJF2016.64.polarity>`_ `PDF <http://www.folklore.ee/folklore/vol64/polarity.pdf>`_
