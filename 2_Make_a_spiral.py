def check(n, nx, ny, matrix) -> int:
    if not (0 <= nx < n and 0 <= ny < n):
        return -1   # выход за пределы диапазона
    else:
        return matrix[nx][ny]   # 1 - если клетка занята, 0 - если свободна

def get_new_direction(d):
    return (d + 1) % 4

def generate_spiral(n: int):
    matrix = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y, d, pd = 0, 0, 0, 1
    dx, dy = directions[d]
    spiral_not_done = True 
    while spiral_not_done:
        matrix[x][y] = 1

        l1 = check(n, x + 2*dx, y + 2*dy, matrix)
        nd = get_new_direction(d)
        ndx, ndy = directions[nd]
        l2 = check(n, x + 2*ndx, y + 2*ndy, matrix)

        if l1 == l2 == 0:   # значит, можно идти дальше
            pass 
        elif (l2 == 0 and l1 == 1) or check(n, x+dx, y+dy, matrix)==-1:       # если нужно повернуть
            if pd == 1:
                spiral_not_done = False    
            pd = 0
            d = get_new_direction(d)
            dx, dy = directions[d]
        elif l1 == -1 and l2 == 0:
            pass 
        else:               # l1 == l2 == 1 или другие значения говорят о том, что спираль готова
            spiral_not_done = False
        x, y  = x + dx, y + dy
        pd += 1
    return matrix

# Проверка
size = 5
spiral = generate_spiral(size)
for row in spiral:
    print(row)
