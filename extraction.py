def extraction(text,pos):
    if(pos<len(text)):
      return text[pos]
    else:
        print("Invalid search key entered")
        
text = input("Enter the text : ")
pos = int(input("Enter the position : "))
print(extraction(text,pos))