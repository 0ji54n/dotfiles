from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("curl -i google.com")
if "Could not resolve host" in my_output:
    print('睊')
else:
    print(' ')
