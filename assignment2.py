a={ }
n = int(input("Enter the no. of Element: "))

for i in range  (n):
    k = input("enter the key:")
    v = input("enter the value:")
    a.update({k:v})
    
print(a)