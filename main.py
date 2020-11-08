import sqlite3

conn = sqlite3.connect('fazenda.db')
cursor = conn.cursor()


def binarySearch():
    sql = 'SELECT ID_vaca FROM produçao_leite WHERE ordenhada'
    cursor.execute(sql)
    result = (cursor.fetchall())
    lista = [list(elements) for elements in result]
    flattened = [val for sublist in lista for val in sublist]
    first = 0
    last = len(flattened) - 1
    found = False
    item = int(input('Digite o ID da vaca que deseja encontrar: '))
    while first <= last and not found:
        midpoint = (first + last)//2
        if flattened[midpoint] == item:
            found = True
        else:
            if item < flattened[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    cursor.close()
    conn.close()
    return print(found)


binarySearch()
