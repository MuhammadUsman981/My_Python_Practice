# Nested for Loops
# color = ["red","green","blue"]
# items = ["book","pen","copy"]

# for color in color:
#     for item in items:
#         print(color,item)
        
# Nested while loop
# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(i,j)
#         j += 1
#     i +=1

# for loop inside while loop
i = 0
while i < 3:
    for j in range(3):
        print(i,j)
    i += 1
# while loop inside for loop
for i in range(3):
    j = 0
    while j < 3:
        print(i,j)
        j += 1
        
     