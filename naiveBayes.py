filepath = "Datasets/naive_bayes_data.txt"

cnt=0
#reading the paragraphs from the file
with open(filepath, encoding="utf8") as fp:  
   data = fp.readlines()

#splitting the paragraph into words and appending each word into the array  
lines = []
for i in range(0, len(data)):
    lines.append(data[i].split())
    
class0 = []
class1 = []

test = []
#dividing the positive class and negative class
for line in range(0, 9531):
    if lines[line][1]=="neg":
        class0.append(lines[line])
    elif lines[line][1]=="pos":
        class1.append(lines[line])
    else:
        print("No such class present")
        break
#splitting the dataset into 80 and 20 percent
for line in range(9531, len(lines)):
    test.append(lines[line])

class0len = len(class0)
class1len = len(class1)
testlen = len(test)

#finding the probability of each word in the paragraph
words0 = {}
words0len = 0
for line in class0:
    for word in line:
        words0len = words0len+1
        if word in words0:
            words0[word] = words0[word]+1
        else:
            words0[word] = 1
        
        
words1 = {}
words1len = 0
for line in class1:
    for word in line:
        words1len = words1len+1
        if word in words1:
            words1[word] = words1[word]+1
        else:
            words1[word] = 1

cnt=0

for line in test:
    prob0 = 1
    prob1 = 1
    probpos=0
    probneg=0
    cls = 0
    for word in line:
        if word in words0:
            prob0=prob0*(words0[word]/words0len + 0.0001)
        if word in words1:
            prob1=prob1*(words1[word]/words1len + 0.0001)
                    
    probpos=prob0*(class0len)/(class0len+class1len)    
    probneg=prob1*(class1len)/(class0len+class1len)
    if probpos>=probneg:
        cls = 0
    else:
        cls = 1
    if line[1]=="pos":
        if cls==0:
            cnt=cnt+1
    if line[1]=="neg":
        if cls==1:
            cnt=cnt+1

accuracy = cnt/testlen
print(accuracy*100)
    
     
        
        
        
        
        
        
        
        
        
