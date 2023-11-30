with open("file.txt", "w") as f:
 while(1==1):
 line=input("enter the lines: ")
 f.write(line)
 f.write("\n")
 choice=input("are you done(Y/N)")
 if(choice.lower() == "y"):
 break
 else:
 pass
 f.close()
 print("Written in file successfully")
with open("file1.txt","r") as g:
 print("Reading the file\n")
 print(g.read())