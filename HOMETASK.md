### Topic 13: Files

#### Task 1
Откройте файл `hw/unsorted_names.txt` в папке данных. Сортируйте имена и 
записывайте их в новый файл `sorted_names.txt`. Каждое имя должно начинаться с новой строки, 
как в следующем примере:
```text
Adele
Adrienne
...
Willodean
Xavier
```

#### Task 2
Реализовать функцию поиска наиболее распространенных слов в файле. 
Используйте файл `hw/lorem_ipsum.txt`. ПРИМЕЧАНИЕ: Помните о точках, запятых, заглавных 
буквах и т.д

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
>>> ['donec', 'etiam', 'aliquam']
```
