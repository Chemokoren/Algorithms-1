"""
Underscorify Substring

In this question you are provided with two strings. The first one, called the main string is the 
longer string. And the smaller string, also called the substring.

The objective of the question is to write a function that will find every instance of the substring in the main 
string and return a new string that's technically the main string with underscores wrapped around 
every instance of the substring.

Conceptual Overview:

    get_locations Function:
        Finds all occurrences of a substring in a string and returns a list of start and end indices for each occurrence.

    collapse_locations Function:
        Merges overlapping or adjacent intervals in the list of locations.

    underscore_string Function:
        Uses the list of locations to underscore the original string.

    underscore_substring Function:
        Combines the process of getting locations and underscoring the string into a single function call.


"""


# O(n + m) time | O(n) space

def underscore_substring(string, substring):
    """
    Underscore specific occurrences of a substring in a string.

    Parameters:
    - string (str): The original string.
    - substring (str): The substring to underscore in the original string.

    Returns:
    - str: The modified string with underscores.
    """
    # Combine the steps to get locations and collapse them into a single call
    locations = collapse_locations(get_locations(string, substring))
    # Use the locations to underscore the original string
    return underscore_string(string, locations)

def get_locations(string, substring):
    """
    Find all occurrences of a substring in a string.

    Parameters:
    - string (str): The original string.
    - substring (str): The substring to find in the original string.

    Returns:
    - list: A list of start and end indices for each occurrence of the substring.
    """
    locations = []
    startIdx = 0
    while startIdx < len(string):
        # Find the next occurrence of the substring in the remaining part of the string
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            # If found, add the start and end indices of the substring to locations
            locations.append([nextIdx, nextIdx + len(substring)])
            # Move the starting index to the next character after the found substring
            startIdx = nextIdx + 1
        else:
            # If no more occurrences are found, break out of the loop
            break
    return locations

def collapse_locations(locations):
    """
    Merge overlapping or adjacent intervals in a list of locations.

    Parameters:
    - locations (list): A list of start and end indices.

    Returns:
    - list: A list of merged or collapsed locations.
    """
    # If there are no locations, return an empty list
    if not len(locations):
        return locations
    
    newLocations = [locations[0]]
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            # If the current location overlaps with the previous one, merge them
            previous[1] = current[1]
        else:
             # If no overlap, add the current location to the newLocations list
            newLocations.append(current)
            previous = current
    return newLocations

def underscore_string(string, locations):
    """
    Underscore specific locations in a string.

    Parameters:
    - string (str): The original string.
    - locations (list): A list of start and end indices to underscore in the original string.

    Returns:
    - str: The modified string with underscores.
    """
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False
    finalChars = []
    i = 0

    # Iterate through the string and the locations simultaneously
    while stringIdx < len(string) or locationsIdx < len(locations):
        if locationsIdx < len(locations) and stringIdx == locations[locationsIdx][i]:
            # If the current character is at a location, add an underscore
            finalChars.append("_")
            # Toggle the inBetweenUnderscores flag
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                # If the underscore is closed, move to the next location
                locationsIdx += 1
            # Switch between start and end indices of the location
            i = 0 if i == 1 else 1
        elif stringIdx < len(string):
             # If not in a location, append the current character from the original string
            finalChars.append(string[stringIdx])
            stringIdx += 1
    # Join the characters to form the final underscored string
    return "".join(finalChars)




print("--------")
print(underscore_substring("test this is a test", "test"))
print(underscore_substring("testthis is a testtest to see if testestest it works", "test"))