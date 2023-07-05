# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# for i in range(1,6):                                        
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# * 
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# * * * * 
# * * *
# * *
# *
# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# 4 4 4 4 
# 3 3 3
# 2 2
# 1
# for i in range(4,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# 1
# 22
# 123
# 4444
# 12345
# 666666
# n=int(input("enter a no of rows: "))
# for i in range(1,n+1):
#     if i%2==0:
#         for j in range(1,i+1):
#             print(i,end='')
#     else:
#         for j in range(1,i+1):
#             print(j,end='')
#     print()