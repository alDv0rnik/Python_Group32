def foo(data, new_value):
    if type(data) is list:
        data.append(new_value)
        return data
    elif type(data) is set:
        data.add(new_value)
        return data
    elif type(data) is str and type(new_value) is str:
        data += new_value
        return data
    elif type(data) is int or type(data) is float or type(data) is bool or type(data) is dict:
        return data

print(foo({1,2}, 3))