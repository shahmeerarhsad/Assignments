import datetime, os, signal, subprocess, sys, time, unittest

def run(command, stdin = None, timeout = 30):
    """
    Runs the specified command using specified standard input (if any) and
    returns the output on success. If the command doesn't return within the
    specified time (in seconds), "__TIMEOUT__" is returned.
    """

    start = datetime.datetime.now()
    process = subprocess.Popen(command.split(),
                               stdin = subprocess.PIPE, 
                               stdout = subprocess.PIPE,
                               stderr = subprocess.STDOUT)
    if not stdin is None:
        process.stdin.write(stdin)
        process.stdin.close()
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return "__TIMEOUT__"
    return process.stdout.read()

class Problem1(unittest.TestCase):

    def test1(self):
        command = "python location.py 48.87 -2.33 37.8 -122.4"
        sought = """loc1 = (48.87, -2.33)
loc2 = (37.8, -122.4)
d(loc1, loc2) = 8701.38954324
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command = "python point.py 0 1 1 0"
        sought = """p1 = (0.0, 1.0)
p2 = (1.0, 0.0)
d(p1, p2) = 1.41421356237
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem3(unittest.TestCase):

    def test1(self):
        command = "python interval.py 3.14"
        sought = """[2.5, 3.5] contains 3.140000
[3.0, 4.0] contains 3.140000
[0.0, 1.0] intersects [0.5, 1.5]
[0.0, 1.0] intersects [1.0, 2.0]
[0.5, 1.5] intersects [1.0, 2.0]
[0.5, 1.5] intersects [1.5, 2.5]
[1.0, 2.0] intersects [1.5, 2.5]
[1.5, 2.5] intersects [2.5, 3.5]
[2.5, 3.5] intersects [3.0, 4.0]
"""
        got = run(command, "0 1 0.5 1.5 1 2 1.5 2.5 2.5 3.5 3 4")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem4(unittest.TestCase):

    def test1(self):
        command = "python rectangle.py 1.01 1.34"
        sought = """Area([0.0, 1.0] x [0.0, 1.0]) = 1.000000
Perimeter([0.0, 1.0] x [0.0, 1.0]) = 4.000000
Area([0.7, 1.2] x [0.9, 1.5]) = 0.300000
Perimeter([0.7, 1.2] x [0.9, 1.5]) = 2.200000
[0.7, 1.2] x [0.9, 1.5] contains (1.010000, 1.340000)
[0.0, 1.0] x [0.0, 1.0] intersects [0.7, 1.2] x [0.9, 1.5]
"""
        got = run(command, "0 1 0 1 0.7 1.2 .9 1.5")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem5(unittest.TestCase):

    def test1(self):
        command = "python rational.py 100"
        sought = """3.13159290356
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

if __name__ == "__main__":
    unittest.main()
