"""
Experiment 2: Strings, Lists, Tuples, and Dictionaries
PostLab: Programming Problem Number 1
Executed by: Dylan Lyle A. Pagkaliwangan
"""
"""
The program computes for the mean, median, and mode of a given integer list
Each function also returns 0 if the list is empty
"""
def average(sample):
    if len(sample) == 0:
        return 0
    ave = 0
    for counter in sample:
        ave = ave + counter
    final = ave/len(sample)
    return final

def mode(sample):
    if len(sample) == 0:
        return 0
    theDictionary = {}
    for word in sample:
        number = theDictionary.get(word, None)
        if number == None:
            theDictionary[word] = 1
        else:
            theDictionary[word] = number + 1
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            print("The mode is", key)
    return theDictionary

def median(sample):
    if len(sample) == 0:
        return 0
    sample.sort()
    midpoint = len(sample) // 2
    print("The median is", end=" ")
    if len(sample) % 2 == 1:
        return sample[midpoint]
    else:
        return (sample[midpoint] + sample[midpoint - 1]) / 2

def main():
    print("The average is", average([45,66,22,10,15,88,15,31,90]))
    print(mode([45,66,22,10,15,88,15,31,90]))
    print(median([45,66,22,10,15,88,15,31,90]))
main()