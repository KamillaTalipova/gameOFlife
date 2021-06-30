import numpy as np
from matplotlib import pyplot as plt
import numpy.random as rand

def next_population(population):
    neighbors = sum([
    np.roll(np.roll(population, -1, 1), 1, 0),
    np.roll(np.roll(population, 1, 1), -1, 0),
    np.roll(np.roll(population, 1, 1), 1, 0),
    np.roll(np.roll(population, -1, 1), -1, 0),
    np.roll(population, 1, 1),
    np.roll(population, -1, 1),
    np.roll(population, 1, 0),
    np.roll(population, -1, 0)
    ])
    return (neighbors == 3) | (population & (neighbors == 2))


def NMP():
    print('enter the dimension of the matrix(N*M)')
    print('enter M')
    M=int(input())
    print('enter N')
    N = int(input())
    print('enter the number k')
    k=int(input())
    population = np.random.randint(0, 2, M * N).reshape(N, M)
    print('field')
    print(population)
    for i in range(k):
        population = next_population(population)
    print('field through k steps')
    print(population)
    print('_____________________________')

def MTPL():
    M = 512
    N = 256
    print('enter the number k')
    k=int(input())
    population = np.random.randint(0, 2, M * N).reshape(N, M)
    plt.matshow(population)
    #plt.show()
    for i in range(k):
        population = next_population(population)
    plt.matshow(population)
    plt.show()

def main():
    #NMP()
    MTPL()
if __name__ == '__main__':
    main()

