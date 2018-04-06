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
        process.stdin.write(bytes(stdin, 'utf-8'))
    process.stdin.close()
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return "__TIMEOUT__"
    result = process.stdout.read().decode("utf-8")
    process.stdout.close()
    return result

class Problem1(unittest.TestCase):

    def test1(self):
        command = "python3 sin.py 60"
        sought = """0.8660254037844385
0.8660254037844386
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command = "python3 distance.py 5"
        sought = """13.0
"""
        got = run(command, "-9 1 10 -1 1 -5 9 6 7 4")
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem3(unittest.TestCase):

    def test1(self):
        command = "python3 palindrome.py bolton"
        sought = """False
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
    def test2(self):
        command = "python3 palindrome.py amanaplanacanalpanama"
        sought = """True
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem4(unittest.TestCase):

    def test1(self):
        command = "python3 reverse.py"
        sought = """question the is that be to not or be to
"""
        got = run(command, "to be or not to be that is the question")
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
class Problem5(unittest.TestCase):

    def test1(self):
        command = "python3 transpose.py"
        sought = """1.0 4.0
2.0 5.0
3.0 6.0
"""
        got = run(command, "2 3 1 2 3 4 5 6")
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

if __name__ == "__main__":
    unittest.main()
