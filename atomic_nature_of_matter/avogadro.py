import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    arr = []
    arr = stdio.readAllFloats()
    P = 0.5e-6
    R = 8.31457
    N = 9.135e-4
    pixels_to_meters = 0.175e-6
    count = 0
    T = 297
    D = 0
    var = 0
    for i in range(len(arr)):
        var += math.pow(arr[i] * pixels_to_meters, 2)
        count += 1
    D = var / (2 * count)
    k = (6*math.pi*D*N*P)/T
    N_A = R/k
    stdio.writef("Boltzman = %.6e\n", k)
    stdio.writef("Avogadro = %.6e\n", N_A)


if __name__ == '__main__':
    main()
