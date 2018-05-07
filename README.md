# GAvI

Simple python progam that creates an inverted index based on TREC precision medicine documents. Then, with the index, is possible to make benchmarking or simple queries. 

requirements:
  sudo apt-get install python3
  sudo pip3 install nltk
  sudo pip3 install matplotlib
  sudo pip3 install npyscreen
  python3
  >>> import nltk
  >>> nltk.download('stopwords')
  >>> nltk.download('punkt')
  >>> nltk.download('averaged_perceptron_tagger')
  >>> nltk.download('universal_tagset')
  ...

documents: http://www.trec-cds.org/2016.html

how to install and execute:
  git clone https://github.com/MurgoloMichele/GAvI.git
  git checkout CLI
  python3 main_CLI.py
