from collections import Counter
with open('input.txt') as f: 
    inp = f.read()

#Defining a function to find all points of a line between p1 and p2
def line(p1, p2):
    output = []
    x1,x2,y1,y2 = p1[0], p2[0], p1[1], p2[1]
    if x1!=x2:
        for x in range(x1, x2+int((x2-x1)/abs(x2-x1)), int((x2-x1)/abs(x2-x1))):
            y = (y1-y2)/(x1-x2) * (x - x1) + y1 
            output.append((int(x),int(y)))
    elif y1!=y2:
        for y in range(y1, y2+int((y2-y1)/abs(y2-y1)), int((y2-y1)/abs(y2-y1))):
            x = (x1-x2)/(y1-y2) * (y-y1) + x1
            output.append((int(x),int(y)))
    return output

coordinates = []
for x in inp.split('\n'):
    p1,p2 = [int(i) for i in x.split(' -> ')[0].split(',')], [int(i) for i in x.split(' -> ')[1].split(',')]
    if p1[0]==p2[0] or p1[1]==p2[1]:
        coordinates += line(p1,p2)

print(len([k for k,v in dict(Counter(coordinates)).items() if v>1]))