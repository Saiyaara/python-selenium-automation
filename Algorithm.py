text_str ="aaabbbcccddd"

print("The original string is :" + text_str)

first_part = text_str[0:len(text_str)//2]
second_part = text_str[len(text_str)//2 if len(text_str)% 2 == 0 else((len(text_str)//2)+ 1):]

print("The first part of the string is : ",  first_part)
print("The second part of the string is : " , second_part)

temp = first_part
first_part = second_part
second_part = temp

print("first_part after swapping is :", first_part)
print("second_part after swapping is :", second_part)

#String1 = "first_part"
#String2 = "second_part"

#String1, String2 = String2, String1

#print(second_part, first_part)