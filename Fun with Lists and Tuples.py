#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#Solution:

Sample_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
  
def Sorted_increasing(Given_sequence):
    return sorted(Given_sequence, key=tuple_last_element)

def tuple_last_element(x):
    return x[-1]
    
print("Given_sequence:",Sample_list)
print("Expected Result:",Sorted_increasing(Sample_list))