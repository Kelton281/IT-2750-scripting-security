#8.9
couple ways to make a rail fence cipher more sophiscated is adding spaces into it's context as chracters for added security.
implementation of nulls in the cipher are optional as well.
#8.14
def wordpop(text, n):
    nwords = []
    words = text.split()
    for word in words:
        if (len(word) >=n):
            nwords.append(word)
    return sorted(nwords, key=len, reverse= True)
text =("please do not sort this text")
print (wordpop(text.lower(), 4))
#8.18
import re
userinput = input("enter a expression")
print(re.findall(r"\b(\w+ing)\b", userinput))
#8.20
import re
sentence = "all and all for one"
findpattren = r"\ba[^\W\d_]*a\b"
print(re.findall(findpattren, sentence))

