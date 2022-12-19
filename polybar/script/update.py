from subprocess import PIPE, run
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("pacman -Qu")
if my_output == "":
    print(u'\ue09a')
else:
    print(u'\uf33d')
