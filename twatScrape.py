#Python 3.x
#Name: TwatScrape
#By: INIT_6
#scrapes twitter for key words and prints the text. 
#TODO: send keyword queries through comand line


import json
import urllib.request
import re

#change the arguments to change search options. 
def main(queries = ['cats','dogs'], results_per_page = '100', language = 'en', num_pages = 4):
    wl = []
    for query in queries:
        for page in range(1, num_pages + 1):
            base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
                 % (urllib.parse.quote_plus(query), results_per_page, language, page)
            wl.extend(getwordlist(base_url))
    uniqWL = uniq(wl)
    for word in uniqWL:
        print( re.sub("^\#|^\@", '', word ) )            

#Takes base_url. Request .json data parse data and returns word list.  
def getwordlist(base_url):
    wordlist = []
    data = urllib.request.urlopen(base_url).read()
    jdata = json.loads(data.decode("ascii")) #have to decode data for loads()
    for lines in jdata['results']: #Results has many items we are only looking at text users said.
        wl = []
        wl = lines['text'].encode("ascii","ignore").split() #for each line split at white space and encode data ignoring any non-ascii char
                    
        for word in wl:
             if clean(word.decode("ascii")) == None:   #fillters out any re you don't want. 
                 wordlist.append(word.decode("ascii")) #if the word doesn't match re function it will append to wordlist[]
    return wordlist                                 

def clean(datass):
    m = re.search("^http://|^https://", datass)  #fillters out any line with url's.
    return m
    
#get uniq out of the string list
def uniq(listobj):
    final = []
    listobj.sort()
    temp = ""
    for item in listobj:
        if item != temp:
            if len(item) > 3:
                final.append(item)
                temp = item	
    return final

main()
