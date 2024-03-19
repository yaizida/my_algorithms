def solution(node, idx):
    # Напишите код функции здесь
    count = 0  # счетчик
    head = node  # Головной элемент
    temp = head  # временный узел - текущий головной элемент
    if idx == 0:
        head = temp.next_item
        return head
    while temp is not None:  # пока элемент temp не None
        if (count+1) == idx:
            temp.next_item = temp.next_item.next_item
        count += 1  # Добовляем к счетчику + 1
        temp = temp.next_item  # И берем следующий элемент
    if temp is None:
        return head
    # "Пееревязываем" ссылку на след. эдемент через 1
    # head.next_item = temp.next_item.next_item
    # print(head)
