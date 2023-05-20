from subprocess import run, TimeoutExpired
from os import path

def AssertTrue(what, message):
    if what == False:
        raise Exception(message)

def AssertEqual(a, b, message):
    AssertTrue(a == b, message)
 
cmd = [ 'python3', '../scripts/boinc/r.py', 'mytest.json' ]
try:
    p = run(cmd, timeout = 100)
except TimeoutExpired:
    print('Timeout expired')

#p.wait()
print(path.exists('mytest_results.json'))
