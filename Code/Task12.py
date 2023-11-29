"""
Напишите рекурсивную функцию для поиска имени, состоящего ровно из 9 букв.
Структура родословной, в которой хранятся данные об именах, имеет древовидную форму:

root = {'name': 'Анна', 'children': [{'name': 'Егор', 'children':
[{'name': 'Мария', 'children': []}]}, {'name': 'Светлана',
'children': [{'name': 'Инга', 'children': [{'name': 'Елизавета',
'children': []}, {'name': 'Антон', 'children': []}]}, {'name': 'Марина', 'children': []}]}]}
"""

root = {'name': 'Анна', 'children': [{'name': 'Егор', 'children':
[{'name': 'Мария', 'children': []}]}, {'name': 'Светлана',
'children': [{'name': 'Инга', 'children': [{'name': 'Елизавета',
'children': []}, {'name': 'Антон', 'children': []}]}, {'name': 'Марина', 'children': []}]}]}


def get_child_name(node: dict) -> str:
    if len(node['name']) == 9:
        return node['name']

    if children := node['children']:
        for child in children:
            if (value := get_child_name(child)) != None:
                return value


print(get_child_name(root))
