def calculate_word_frequencies(my_string):
    dic ={}
    my_string =my_string.lower().split()
    exceptions = [',','.']
    new_arr =[]
    for i in my_string:
        if i in exceptions:
            continue
        new_arr.append(i)    
    # string_arr =my_string.split()
    for i in new_arr:
        if i not in dic:
            dic[i] =1
        else:
            dic[i] +=1
            
    return dic


if __name__ == "__main__":
    my_string = "My cat name is Surkia. Surkia is a very fancy cat. Surkia likes to meow to get attention, but he does that very kindly."
    results = calculate_word_frequencies(my_string)
    print(results)