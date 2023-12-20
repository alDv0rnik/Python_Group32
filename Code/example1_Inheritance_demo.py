"""
Define class my_list inherited from List. Add new method is_even_length.
"""


class MyList(list):

    def is_even_length(self):
        return True if self.__len__() % 2 == 0 else False


new_list = MyList()
new_list.append(1)
new_list.append(2)
new_list.append(3)
# new_list.append(4)

print(new_list.is_even_length())