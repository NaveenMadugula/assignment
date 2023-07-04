#Calculate the sum of all numbers from 1 to a given number
# number = int(input('Enter a number: '))
# total = 0
# for i in range(1, number+1):
#     total+=i
# print("The sum of 1 to", number, "is:", total)

#Write a program to print multiplication table of a given number
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     result = num*i
#     print(f"{num} X {i} = {result}")


#Display numbers from a list using loop
# num = [1,2,3,4,89,45,60,89,90]
# print("Numbers in the list are ")
# for number in num:
#     print(number)

#Count the total number of digits in a number 
# num = int(input("enter a number:"))
# print("The length of the number is: ",len(str(num)))

#Print list in reverse order using a loop
# li = [12,34,56,90,89,45,39,"naveen"]
# my_li = []
# for value in li:
#     my_li = [value] + my_li
# print("list in reverse order is: ",my_li)


#Display numbers from -10 to -1 using for loop
# for num in range(-10,0):
#     print(num)


#Use else block to display a message “Done” after successful execution of for loop
# for num in range(1,20):
#     print(num)
# else:
#     print("Done")


#Write a program to display all prime numbers within a range
# value_1 = int(input ("Please, Enter the Value_1 Range Value: "))  
# value_2 = int(input ("Please, Enter the Value_2 Range Value: "))  
# print ("The Prime Numbers in the range are: ")  
# for number in range (value_1, value_2 + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number)  