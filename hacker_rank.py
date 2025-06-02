s = input()

lower_list = []
upper_list = []
odd_list = []
even_list = []
final_list = []

for item in s:
    if item.isupper():
        upper_list.append(item)
    elif item.islower():
        lower_list.append(item)
    elif item.isdigit() :
        if int(item) % 2 == 0 :
            even_list.append(str(item))
        else:
            odd_list.append(str(item))

lower_list = sorted(lower_list)
upper_list = sorted(upper_list)
odd_list = sorted(odd_list)
even_list = sorted(even_list)
final_list = lower_list + upper_list + odd_list + even_list
print("".join(final_list))
            
# Sorting1234
# ginortS1324
