def add_mean(x, *data):
    return x + sum(data)/float(len(data))


def handle_info(*person_info, **person_additional_info):
    print(*person_info,  **person_additional_info)


person_info = ('Mike', 35)
person_additional_info = {
    'sex': 'male',
    'friends': ('Kate',)
}
info = dict(sex='male', friends=('Kate', 'Jack', ))

handle_info(*person_info, info)

