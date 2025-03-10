# Примеры / Examples
Просто случайные решённые задачи. / Just a random solved tasks.


## 1. Консольное приложение, которое выводит на экран "бабочку" заданного размера N.
Увидел такой пример в телеграме: \
![Задачи в группе на ~60 тыс. подписчиков](https://github.com/user-attachments/assets/19227596-d23b-4c88-8685-14fad6670a81) \
Понял, что можно сделать проще. Сделал :) \
Результат: \
![мой код](https://github.com/user-attachments/assets/46e0792b-b047-4c6f-b271-0ae383d858b9) \
![вывод](https://github.com/user-attachments/assets/34eb7c5d-940d-409e-a22c-df2e98a7cfd3) \
Логика решения: \
Бабочка имеет размеры 2N * (2N-1). \
Идём по каждому символу и определяем, относится текущий символ к бабочке или нет, пользуясь схемой, и выводим соответствующий символ к консоль. \
![схема](https://github.com/user-attachments/assets/01f030a7-cb3c-40a3-851c-3666db3d57b7) \
Сложность алгоритма О(N^2). \
Т.к. бабочка 2D-шная, то быстрее, чем за N^2 её вывести не получится, но можно оптимизировать вывод за счёт выделения дополнительнйо памяти.

## 2. Make a spiral
![image](https://github.com/user-attachments/assets/73d2893c-cd17-4f54-98f6-006c029761ec)
Примеры методов \
![image](https://github.com/user-attachments/assets/cad63008-aa2a-47fa-900e-aa8f9b2136c9)
Результат: \
![image](https://github.com/user-attachments/assets/0e224ae5-2e0d-402d-93fb-52b46325ec51)
