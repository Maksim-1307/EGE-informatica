def win(pos):
    if sum(pos) >= 150: return True
    return False
def moves(pos):
    return (pos[0]+2, pos[1]), (pos[0], pos[1]+2), (pos[0]*3, pos[1]), (pos[0], pos[1]*3)
def game(pos, n):
    if win(pos):
        if n % 2 == 1:
            return False
        else:
            return True
    if n > 4: return False
    if n % 2 == 1:
        return any(game(m, n+1) for m in moves(pos))
    else:
        return all(game(m, n+1) for m in moves(pos))

def game2(pos, n):
    if win(pos):
        if n % 2 == 1:
            return False
        else:
            return True
    if n > 2: return False
    if n % 2 == 1:
        return any(game2(m, n+1) for m in moves(pos))
    else:
        return all(game2(m, n+1) for m in moves(pos))

for N in range(133):
    if game((16, N), 0) and not game2((16, N), 0):
        print(N)