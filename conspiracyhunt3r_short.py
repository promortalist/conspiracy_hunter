def splitkeep(s, delimiter):
    split = s.split(delimiter)
    return [substr + delimiter for substr in split[:-1]] + [split[-1]]

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

from bs4 import BeautifulSoup    
import ebooklib
import re
from ebooklib import epub
def epub2thtml(epub_path):    
    book = epub.read_epub(epub_path)
    chapters = []    
    for item in book.get_items():
      if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item.get_content())    
    return chapters


def epub3thtml(epub_path):    
    book = epub.read_epub(epub_path)
    chapters = []    
    #for item in book.get_items():
    #    print(item)
    for item in book.get_items():
        if any(re.findall(r'Chapter2|Chapter02|chapter2|chapter02', str(item), re.IGNORECASE)):
           break
        #print(item)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
           chapters.append(item.get_content())
    return chapters
 
def chap2text(chap):
    output = ''    
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)    
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
   chapters = epub2thtml(epub_path)
   ttext = thtml2ttext(chapters)     
   return ttext


def epub3text(epub_path):
   chapters = epub3thtml(epub_path)
   ttext = thtml2ttext(chapters)     
   return ttext


blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]
shamingwords = [" icy ","ice","frozen","chill","hockey","arctic","Antarctica","Siberia","siberian","freeze","ice-cream","suck","sucking","sucks","windows","stick","finger","red","dark","child","children","nail","fetish","weird","strange","odd",]

icewords = [" icy ","ice","frozen","chill","hockey","arctic","Antarctica","Siberia","siberian","freeze","ice-cream","suck","sucking","sucks","cool","cold war","cold","fellatio","blowjob","oral sex","princess","queen","throat","air","breath","breathing","breaths"]
def shaming_hunt3r(word):
    i = 0
    while i != len(shamingwords):
        if shamingwords[i] in str(word):
           print("--------------------------------------------")
           print("Found "+str(shamingwords[i]))
           print("--------------------------------------------")
           print("Source: "+str(word))
        i = i + 1


def sh4ming_hunt3r(word):
    i = 0
    while i != len(shamingwords):
         shamingword = shamingwords[i]
         my_regex = r"\b(?=\w)" + re.escape(shamingword) + r"\b(?!\w)"
         if re.search(my_regex, str(word), re.IGNORECASE):
           print("--------------------------------------------")
           #print("Found "+str(shamingwords[i]))
           print("--------------------------------------------")
           print("Source: "+str(word))
         i = i + 1

# budowa statystyk

# 3 glowne kategorie

# ice princess
# finger,car,children..
# red, darkness

# może stworzyc 3 funkcje grupujące, budujące dowody i zliczające np. wystapienie słów "lodowych" w pojedynczej ksiazce i potem zlicza liczbę ksiazek z "lodem".
# już po paru tysiacach książek powinnien być jawny pattern

# stworzyc jeden record sqlite jako long string ze slownikiem o polach iceword + quotation dla danej ksiazki, pozniej konwertowac string do slownika, do analizy dalszych statystyk, np. aby zliczyc ile setek razy wystapi w ksiazkach slowo
# "ice-cream" albo "ice"

# icedict = {'ice':["quote1","quote2","quote3"],'cool':["quote1","quote2","quote3"]}


#if iceword in icedict.keys():
#     icedict[iceword].append("quote4")
#else:
# icedict[iceword]=[]
# icedict[iceword].append("quote4")

#import json
 
# initializing string
#test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
 
# printing original string
#print("The original string : " + str(test_string))
 
# using json.loads()
# convert dictionary string to dictionary
#res = json.loads(test_string)
 
# print result
#print("The converted dictionary : " + str(res))



def ice_sh4ming_2(word):
    i = 0
    counter = 0
    icedict = {}
    while i != len(icewords):
         shamingword = icewords[i]
         my_regex = r"\b(?=\w)" + re.escape(shamingword) + r"\b(?!\w)"
         if re.search(my_regex, str(word), re.IGNORECASE):
           print("--------------------------------------------")
           print("Found "+str(shamingword))
           # add to dictionary icedict
           #str(shamingword)
           counter = counter + 1
           print("--------------------------------------------")
           print("Source: "+str(word))
           # add to dictionary icedict
           if shamingword in icedict.keys():
               icedict[shamingword].append(word)
           else:
               icedict[shamingword]=[]
               icedict[shamingword].append(word)
         i = i + 1
    return counter, icedict

def ice_sh4m1ng(word):
    i = 0
    while i != len(icewords):
         shamingword = icewords[i]
         my_regex = r"\b(?=\w)" + re.escape(shamingword) + r"\b(?!\w)"
         if re.search(my_regex, str(word), re.IGNORECASE):
           print("--------------------------------------------")
           print("Found "+str(shamingword))
           print("--------------------------------------------")
           print("Source: "+str(word))
         i = i + 1
    return shamingwords, word

def ice_sh4ming(word):
    i = 0
    counter1 = 0
    icedict = {}
    while i != len(icewords):
         shamingword = icewords[i]
         my_regex = r"\b(?=\w)" + re.escape(shamingword) + r"\b(?!\w)"
         if re.search(my_regex, str(word), re.IGNORECASE):
          # print("--------------------------------------------")
          # print("Found "+str(shamingword))
           # add to dictionary icedict
           #str(shamingword)
           counter1 = counter1 + 1
          # print("--------------------------------------------")
          # print("Source: "+str(word))
           # add to dictionary icedict
           if shamingword in icedict.keys():
               icedict[shamingword].append(word)
           else:
               icedict[shamingword]=[]
               icedict[shamingword].append(word)
         i = i + 1
    return counter1, icedict

#sys.argv[0]

def ksiazka(epub): 
  e = epub3text(epub)
  e2 = ''.join(e)
  e2b = e2.replace("et al.","et al ")
  e3 = splitkeep(e2b, ".")
  metaicedict = {}
  for group in chunker(e3, 1): 
      results = ice_sh4ming(group)
      icedict = results[1]
      for shamingword in icedict:
          #print(shamingword)
          if shamingword in metaicedict.keys():
               metaicedict[shamingword].append(icedict[shamingword])
          else:
               metaicedict[shamingword]=[]
               metaicedict[shamingword].append(icedict[shamingword])
  print (metaicedict.keys())

from pathfinder import find_paths
paths = find_paths(".", fnmatch="*.epub")
try:
 for path in paths:
     book = epub.read_epub(path)
     author = book.get_metadata('DC', 'creator')
     print(author[0][0])
     title = book.get_metadata('DC', 'title')
     print(title[0][0])
     ksiazka(path)
     print("-------------------------------------------------------")
except AttributeError:
 pass
