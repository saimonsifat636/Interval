import re

text="today is a good day , I will do my best to get my output 100% today . I wanna be that much good so that no one can deny me "

match=re.search('100%',text)        #this will return the object with first and ending index.
print(match)
if match:
    print("starting index: ",match.start())     #  return the starting index.
    print("ending index: ", match.end())     # return the ending index.
    print("patten is found.")

print(re.findall('today',text,re.IGNORECASE))     # this will return all the occurance of that word.  "re.IGNORECASE" ->  this will check all the cases .
new_text=re.sub('today','fuc*********', text)     # this will replace all the word "today "  to "fuc********"  .
print(new_text)