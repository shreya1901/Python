from collections import Counter
in_str=input("Enter string : ")
freq_char=Counter(in_str)
print("Per charecter freqency in string '{}' is \n {}".format(in_str,str(freq_char)))
