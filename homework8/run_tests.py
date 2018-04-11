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
        command = "python wc_complement.py ACTGACG"
        sought = """TGACTGC
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command = "python domain_type.py http://www.swamiiyer.net/cs110/"
        sought = """net
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem3(unittest.TestCase):

    def test1(self):
        command = "python password_checker.py Abcde1fg"
        sought = """False
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test2(self):
        command = "python password_checker.py Abcde1@g"
        sought = """True
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem4(unittest.TestCase):

    def test1(self):
        command = "python set_distance.py b,c a,b,c,d"
        sought = """0.5
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test2(self):
        command = "python set_distance.py 7,3,2,4,1 4,1,9,7,5"
        sought = """0.571428571429
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

class Problem5(unittest.TestCase):

    def test1(self):
        command = "python word_frequencies.py"
        sought = """of -> 2
it -> 2
times -> 2
the -> 2
was -> 2
worst -> 1
best -> 1
"""
        got = run(command, "it was the best of times it was the worst of times")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

if __name__ == "__main__":
    unittest.main()
