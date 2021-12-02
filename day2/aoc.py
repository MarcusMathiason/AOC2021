input_file = open('day2\input2.txt')

def forward(x, c):
    print(f'Forward {x} steps')
    c[0] += x
    return c

def up(y, c):
    print(f'Up {y} steps')
    c[1] -= y
    return c

def down(y, c):
    print(f'Down {y} steps')
    c[1] += y
    return c

def main():
    coords = [0,0]
    for x in input_file.readlines():
        x = x.split(" ")
        coords = eval(f'{x[0]}({x[1]},{coords})')
    print(f'xPos: {coords[0]}, yPos: {coords[1]}, Multiplied: {coords[0]*coords[1]}')
    return

if __name__ == "__main__":
    main()