#Program for calculating the number of times "the" and "that" comes in file "story.txt"
#The file should be in .txt format only


a=open("story.txt").readlines()     #you can change the story.txt file to your choice file
b,c,d=0,0,0
for i in range (len(a)):
  b=a[i].split(" ")
  if "the" in b:
    c+=1
  elif "that" in b:
    d+=1
print("the number of times the comes is:",c)
print("the number of times that comes is:",d)
