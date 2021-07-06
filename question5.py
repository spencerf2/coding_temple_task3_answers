# Question 5
# ----------------------------------------------------------------------
# Write a function to check to see if all numbers in list are 
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive 
# numbers, but [1,2,4,5] are not consecutive numbers. The return should 
# be boolean Type.
# ----------------------------------------------------------------------
# def is_consecutive(a_list):

def is_consecutive(a_list):
    try:
        min_num = min(a_list)
        max_num = max(a_list)
    except ValueError:  # If value error then sequence is empty and
        return False    # thus not consecutive
    if min_num == a_list[0] and max_num == a_list[len(a_list) - 1]:
        for item in a_list:
            n1 = item
            try:
                n2 = a_list[item - min_num]
            except IndexError:  # If (item - min_num) is outside index
                return False    # the list is not consecutive
            if item != max_num and n1 == n2:
                pass
            elif item == max_num:
                return True
            else:
                return False                
    else:
        return False

t_list = [-677,-666,-665,-664]
print(is_consecutive(t_list))