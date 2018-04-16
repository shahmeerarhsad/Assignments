import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():

    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    for i in range(4,len(sys.argv) - 1):
        pic1 = Picture(sys.argv[i])
        pic2 = Picture(sys.argv[i+1])
        blobscan = BlobFinder(pic1,tau)
        blobscan2 = BlobFinder(pic2,tau)
        blob = blobscan.getBeads(P)
        blob2 = blobscan2.getBeads(P)
        for i in range(len(blob2)):
            least = 0.0000
            first = True
            for j in range(len(blob)):
                b = blob2[i]
                bb = blob[j]
                distance = b.distanceTo(bb)
                if(distance <= delta and first):
                    least = distance
                    first = False
                elif(distance <= delta and distance < least):
                    least = distance
            if(least>0):
                    stdio.writef('%s\n', round(least,4))

    stdio.write('\n')


if __name__ == '__main__':
    main()


