def new_approach(string):
    return ' '.join([word[::-1] for word in
                     string.split(' ')])

def new_trial(sentence):
    list_of_string = [i for i in sentence.split(" ")]
    list_of_string = list(reversed(list_of_string))
    new_list_of_string= " ".join(list_of_string)
    Finalresult = ""
    for i in range(len(new_list_of_string)):
        change_case = reverse_words_order_and_swap_cases(new_list_of_string[i])
        Finalresult +=change_case
    print(Finalresult)
    # print(list_of_string)


import re

def reverse_word(sentence):
    temp = ""
    pattern = re.compile(r'(\W+)')
    result = pattern.split(sentence)
    for i in result:
        p = re.compile("^[a-zA-Z0-9]+$")
        if p.match(i):
            i = i[::-1]
        temp += i
    return temp


def reverse_words_order_and_swap_cases(sentence):
    list_of_string = [i for i in sentence.split(" ")]
    list_of_string = list(reversed(list_of_string))
    new_list_of_string= " ".join(list_of_string)
    Finalresult = ""
    for i in range(len(new_list_of_string)):
        change_case = change_letter_case(new_list_of_string[i])
        Finalresult +=change_case
    return Finalresult

def change_letter_case(sentence):
    new_sentence=""
    for i in range(len(sentence)):
        if(sentence[i].isupper()):
            new_sentence +=sentence[i].lower()
        if (sentence[i].islower()):
            new_sentence +=sentence[i].upper()
        if (sentence[i] ==" "):
            new_sentence +="".join(sentence[i])
    return new_sentence

def my_info(sentence):
    print(sentence[2:])
    print(sentence[:4])
    print(sentence[:])

def anii_():
    string_val ='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
    starting_point =string_val.find('@')
    end_point =string_val.find(' ',starting_point)
    return string_val[starting_point+1 :end_point]

print(anii_())
# my_info("cominghome")
# print(reverse_words_order_and_swap_cases("fUN doinG"))
#

