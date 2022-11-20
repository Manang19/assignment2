
def last(n):
    return n[-1] 
  
def sort(tuples):
    return sorted(tuples, key=last)
  
a=[ ]
n = int(input("Enter the no. of Element: "))

for i in range  (n):
    k = int(input("enter the value1:"))
    v = int(input("enter the value2:"))
    a.append ((k,v))

print(a)

print("Sorted:")
print(sort(a))




