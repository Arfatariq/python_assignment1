#text analyzer 
def  text_analyzer():
    text=input('enter some text :')
    print('text in uppercase :',text.upper())
    print('text length :',len(text))
    print('fitst character of the text :',text[0])
    print('last character of the text :',text[-1])
    
text_analyzer()

#story function
def make_story():
    name=input("enter a name :")
    place=input("enter a place :")
    object =input("enter a object :")
    feeling=input("enter a feeling:")
    print('A short Story :', name + ' went to ' + place + ' with a ' + object + ' and felt very ' + feeling)

    
make_story()

#word formatter
def format_word(word):
    print('word in titlecase:',word.title())
    print('reverse word :',word[::-1])
    word=word.replace('a',"*")
    word=word.replace('e',"*")
    word=word.replace('i',"*")
    word=word.replace('o',"*")
    word=word.replace('u',"*")
    
    print('replaced words :',word)

format_word('education')
  
  
  
  





   

