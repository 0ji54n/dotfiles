from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("curl -i google.com")
if len(my_output) > 1:
    print(' ')
else:
    print('睊')
