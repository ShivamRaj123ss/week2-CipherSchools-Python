name = "Shivam"
if name == "Shivam" or name == "shivam":
    print("You are Shivam")
elif name == "Mohit" or name == "mohit":
    print("You are Mohit")
else:
    print("You are not Shivam or Mohit")

#while
i=0
while i<11:
    print("hello Shivam")
    i+=1

# for loop
for i in range(1,25,2):
    print(i)

#break
for i in range(1,11):
    if i == 5:
        break
    print(i)

# continue
for i in range(1,11):
    if i==6:
        continue
    print(i)

for i in "Shivam":
    print(i)