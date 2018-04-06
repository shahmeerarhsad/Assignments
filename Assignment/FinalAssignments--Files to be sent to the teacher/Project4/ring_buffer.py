"""
ring_buffer.py

Models a ring buffer.
"""

import sys
import stdio


def create(capacity):
    """
    Create and return a ring buffer, with the given maximum capacity and
    with all elements initialized to None. A ring buffer is represented as
    a list of four elements: the buffer (buff) itself as a list; number of
    elements (size) currently in buff; the index (first) of the least
    recently inserted item; and the index (last) one beyond the most recently
    inserted item.
    """
    buff = [None] * capacity
    last = 0
    first = 0
    size = 0
    return [buff, last, first, size]


def capacity(rb):
    """
    Return the capacity of the ring buffer.
    """
    return len(rb[0])


def size(rb):
    """
    Return the number of items currently in the buffer rb.
    """
    return rb[3]


def is_empty(rb):
    """
    Return True if the buffer rb is empty and False otherwise.
    """
    return True if rb[3] == 0 else False


def is_full(rb):
    """
    Return True if the buffer rb is full and False otherwise.
    """
    return True if len(rb) == rb[1] - rb[2] else False


def enqueue(rb, x):
    """
    Add item x to the end of the buffer rb.
    """
    if (len(rb[0]) == (rb[3])):
        msg = 'Error: cannot enqueue a full buffer'
        sys.exit(msg)

    else:
        rb[0][rb[1]] = x
        if(rb[1] + 1 == len(rb[0])):
            rb[1] = 0
        else:
            rb[1] = rb[1] + 1
        rb[3] = rb[3] + 1


def dequeue(rb):
    """
    Delete and return item from the front of the buffer rb.
    """
    if (is_empty(rb)):
        msg = 'Error: cannot dequeue an empty buffer'
        sys.exit(msg)
    else:
        ret_val = rb[0][rb[2]]
        rb[0][rb[2]] = None
        rb[3] = rb[3] - 1
        if(rb[2] + 1 == len(rb[0])):
            rb[2] = 0
        else:
            rb[2] = rb[2] + 1
        return ret_val


def peek(rb):
    """
    Return (but do not delete) item from the front of the buffer rb.
    """
    return rb[0][rb[2]]


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    rb = create(N)
    for i in range(1, N + 1):
        enqueue(rb, i)
    t = dequeue(rb)
    enqueue(rb, t)
    size(rb)
    stdio.writef('Size after wrap-around is %d\n', size(rb))
    while size(rb) >= 2:
        x = dequeue(rb)
        y = dequeue(rb)
        enqueue(rb, x + y)
    stdio.writeln(peek(rb))


if __name__ == '__main__':
    _main()
