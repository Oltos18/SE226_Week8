import math

def find_common(list_1, list_2):
    list_1=dict.fromkeys(list_1)
    list_2=dict.fromkeys(list_2)
    result_dict=dict(list_1.items() & list_2.items())
    return list(result_dict)

def is_palindromes(list_1):
    result_list=[]
    list_1=list(list_1)
    for x in list_1:
        if x==x[::-1]:
            result_list.append(x)
    return result_list

def return_primes(list_1):
    result_list=[]
    list_1=sorted(list(list_1))
    number =list_1[-1]
    prime_number = []

    for i in range(2, number + 1):
        prime_number.append(i)
    i = 2
    while i <= int(math.sqrt(number)):
        if i in prime_number:
            for j in range(i * 2, number + 1, i):
                if j in prime_number:
                    prime_number.remove(j)
        i = i + 1

    for x in list_1:
        for y in prime_number:
            if x>y:
                break
            if x==y:
                result_list.append(x)

def anagrams(word, list_strings):
    list_strings=list(list_strings)
    word_list_form=[]
    list_strings_list=[]
    temp_list=[]
    output_list=[]
    
    for x in word:
        word_list_form.append(x)
    word_list_form.sort()
    
    for y in list_strings:
        for z in y:
            temp_list.append(z)
        temp_list.sort()
        list_strings_list.append(temp_list)
        temp_list.clear()
    
    for y in list_strings_list:
        for z in len(y):
            if(word_list_form[z]!=y[z]):
                break
            output_list.append(y)

    return output_list