# Question 1
def hello_name(user_name): 
    print("Hello "+user_name.title()+"!")
hello_name("Halim")

#Question 2
for num in range(0,101): 
    if num % 2 != 0:  
        print(num)

#Question 3
def max_num_in_list(a_list): 
    max = a_list[0]
    for x in a_list:
        if x > max: 
            max = x
    return max

num1 = [1,2,3,5,4,9,12,6,8]
print(max_num_in_list(num1))

#Question 4
def is_leap_year(a_year): 
    if a_year % 4 != 0: 
        return print("False")
    else: 
        return print("True")

is_leap_year(2020)

#Question 5
def is_consecutive(a_list): 
    i = 0 
    status = True
    while i < len(a_list)-1: 
        if a_list[i] + 1 == a_list[i + 1]: 
            i += 1 
        else: 
            status: False 
            break
    print(status)

test = [1092837456]
is_consecutive(test)
