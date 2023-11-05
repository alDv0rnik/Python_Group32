"""
Вы ведете счет в бейсбольном матче по странным правилам. Игра состоит из нескольких раундов,
где результаты прошлых раундов могут повлиять на результаты будущих раундов.
В начале игры вы начинаете с пустой записью. Вам дан список строк ops, где ops[i] — это i-я операция,
 которую вы должны применить к записи, и она является одной из следующих:
    Целое число x. Запишите новую оценку x.
    "+" - Запишите новую оценку, которая является суммой двух предыдущих оценок. Гарантируется, что всегда будет два предыдущих результата.
    "D" - Запишите новый счет, который в два раза превышает предыдущий. Гарантируется, что всегда будет предыдущий счет.
    "C" - аннулировать предыдущий счет, удаляя его из записи. Гарантируется, что всегда будет предыдущий счет.

вернуть сумму всех баллов записи
"""

