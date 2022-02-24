from audioop import reverse
import re

def calculate_frequencies(string):
    # A-Za-z0-9 vs \w. First doesn't work with Unicode strings
    string = re.sub(r'[^\w\s]+','',string).lower().strip()
    words = string.split()

    frequencies ={}
    for word in words:
        if not word in frequencies: # .keys()
            frequencies[word] = 1
        else:
            frequencies[word] += 1
    frequencies = dict(
        sorted(frequencies.items(),
        reverse=True,
        key=lambda frequencies: frequencies[1]))
    return frequencies


# Tuple list version
def calculate_frequencies_tl(string):
    #A-Za-z0-9 vs \w. First doesn't work with Unicode strings
    string = re.sub(r'[^\w\s]+','',string).lower().strip()
    #words = re.split('',string)
    words =string.split()

    frequencies =[]
    for new_word in words:
        matches =[(_word,_freq) for(_word, _freq) in frequencies if _word == new_word]

        if matches == []:
            frequencies.append((new_word, 1))
        else:
            index = frequencies.index(matches[0])
            (_word, freq) = matches[0]
            frequencies[index] =(new_word, freq+1)
    frequencies.sort(reverse=True, key=lambda x:x[1])
    return frequencies


def calculate_word_frequencies_mine(my_string):
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
    string = "One two three two three Three."
    res = calculate_frequencies(string)
    print(res)

    my_string = "My cat name is Surkia. Surkia is a very fancy cat. Surkia likes to meow to get attention, but he does that very kindly."
    results = calculate_frequencies(my_string)
    print(results)
