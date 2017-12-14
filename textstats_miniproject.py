
# coding: utf-8

# In[1]:

def getTokens(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a list of tokenized words.
    Symbols are separated out, and upper case is lowered.
    """
    sym = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    new = txt.lower()
    for s in sym :
        new = new.replace(s, " ")
    return new.split()

def getTypeFreq(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a frequency count dictionary.
    KEY is a word, VALUE is its frequency count.
    """
    Freq = {}
    for w in getTokens(txt) :
        if w not in Freq :
            Freq[w] = 1
        else :
            Freq[w] += 1
    return Freq

def getTypes(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a alphabetically sorted list of unique word types.
    """ 
    x = getTypeFreq(txt)
    return sorted(x.keys())

def getXLengthWords(wtypes, x):
    """Takes a list of unique words (= word types) and integer x as
    arguments. Returns a sorted list of words whose length is at least x.
    """
    lengthwords = []
    for w in getTypes(wtypes) :
        if len(w) >= x :
            lengthwords.append(w)
    return lengthwords

def getXFreqWords(freqdi, x):
    """Takes a word frequency dictionary and integer x as arguments.
    Returns a sorted list of words that are at least x in frequency.
    """
    # [4] Complete this function. YOUR CODE BELOW.
    Freqwords = []
    for (k, v) in getTypeFreq(freqdi).items() :
        if v >= x :
            Freqwords.append(k)
    return sorted(Freqwords)

def textstats(fox):
    "A void function that demonstrates how the functions are used."
    foxtoks = getTokens(fox)      # Function-internal objects:
    foxtypes = getTypes(fox)      #   not accessible from IDLE shell!
    foxfreq = getTypeFreq(fox)    # You can however retrace the steps 
                                  #   to re-create these objects. 
    print('There are', len(foxtoks), 'word tokens in ')
    print('There are', len(foxtypes), 'unique word types in .')
    print(' ')
    print('Words that are at least 10-characters long: ')
    for x in getXLengthWords(fox, 10) :
        print(x + ' has ', len(x), 'characters')
     
    print(' ')
    
    print('Words with 10 or higher frequency: ')
    for w in getXFreqWords(fox, 10) :
        print(' ', "'"+w+"'", 'occurs', foxfreq[w], 'times.')
    
    print(' ')
    
    print('Words with Frequency.')
    for (k, v) in getTypeFreq(fox).items() :
        print(' ', "'"+k+"'", 'occurs ', v, 'times.')
    
def getWord2Grams(wds) :
    gram2 = []
    TokenWDS = getTokens(wds)
    for i in range(len(TokenWDS)-1) :
        gram1 = TokenWDS[i:i+2]
        gram2.append(tuple(gram1))
    return gram2
       
def getWord3Grams(wds) :
    gram3 = []
    TokenWDS = getTokens(wds)
    for i in range(len(TokenWDS)-2) :
        gram1 = TokenWDS[i:i+3]
        gram3.append(tuple(gram1))
    return gram3


def getFreq(li):
    "Takes a list as input, returns a dictionary of frequency count."
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] += 1
    return di

def T2wordbiggrams(txt) :
    wordgrams = getWord2Grams(txt)
    getFr = getFreq(wordgrams)
    print('Top 20 word bigrams by frequency (descending order):')
    for x in sorted(getFr, key=getFr.get, reverse=True)[:20]:
        print(x, getFr[x])
        
def T3wordbiggrams(txt) :
    wordgrams = getWord3Grams(txt)
    getFr = getFreq(wordgrams)
    print('Top 20 word trigrams by frequency (descending order):')
    for x in sorted(getFr, key=getFr.get, reverse=True)[:20]:
        print(x, getFr[x])