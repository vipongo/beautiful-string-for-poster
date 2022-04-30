"""
This function take in argument a file that contains a list of name and then creates a single string separating all names with " | "
It is possible to also add a separating argument in the case there are multiple name in the same line
Example: 
Rebelion
Andy the Core; MBK
Act of Rage
Warface
Rooler

becomes 
Rebelion | Andy the Core | MBK | Act of Rage | Warface | Rooler

"""

def sort_list(filename, separating_argument=""):
    f = open(filename, "r")
    unsorted_list = f.read().splitlines() 
    perfect_string = ""
    final_list = []

    for element in unsorted_list:
        current_elements = []
        all_elements = element.split(separating_argument)

        for names in all_elements:
            current_elements.append(names.strip())

        for item in current_elements:
            if item not in final_list:
                final_list.append(item)

    for name in final_list:
        perfect_string = perfect_string + name + " | "
        
    return perfect_string

#add the filename and optionnal separator you want 
print(sort_list("test.txt", ";"))
