create= open("text.txt","w")

while True:
   sentence = input("enter the sentence :")
   word=""
   for i in range(len(sentence)):
      if sentence[i:i+3]=="...":
         break
      #elif sentence[i]==".":
         #break
      word = word + sentence[i:i+1]
   create.write(word)
   if "..." in sentence:
      break
  # elif "." in sentence:
  #    break


create.close()
st1 = open("text.txt").read()
print("text: "+st1)
create.close()