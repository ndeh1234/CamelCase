s = input("Enter a sentence : ")  # Taking input of sentence
str_arr = s.split()  # splitting the input sentence into words
result = ""  # initializing result as empty string
result += str_arr[0].lower()  # Converting first word ( word at index 0 ) of the input sentence into its lowercase
for i in str_arr[1:]:  #starting iterating from index 1 and onwards
    result += (i.capitalize())  # Capitalizing rest of the words

print("Output : ", result)  # printing the required resultant string





