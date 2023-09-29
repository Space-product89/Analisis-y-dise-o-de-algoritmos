print('TORRES DE HANOI')
def towerH(n,orgn,dst,aux):
    if n==1:
        print ('Mover disco', n, 'a la pila', dst)
        return

    else:
        towerH(n-1,orgn,dst,aux)
        print('mover disco', n, 'a la pila', aux)
        towerH(n-1,orgn,dst,aux)
        
n = 3
towerH(n, 'A', 'B', 'C')