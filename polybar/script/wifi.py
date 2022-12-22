from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("nmcli radio wifi")
if "disabled" in my_output:
    print('睊')
else:
    print(' ')
