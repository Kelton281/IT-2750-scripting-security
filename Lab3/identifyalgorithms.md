def encrypt(plainText ,key):  
  alphabet = "abcdefghijklmnopqrstuvwxyz"  
  plainText = plainText.lower ()  
  cipherText = ""  

  for ch in plainText:  
      idx = alphabet.find(ch)  
      cipherText = cipherText + key[idx]  
  return cipherText  
  #substitution cipher
  
  def scramble2Encrypt(plainText):  
  evenChars = ""  
  oddChars = ""  
  charCount = 0  

  for ch in plainText:  
      if charCount % 2 == 0:  
          evenChars = evenChars + ch  
      else:  
          oddChars = oddChars + ch  
    charCount = charCount + 1  
  cipherText = oddChars + evenChars  
  return cipherText  
  #Transition cipher