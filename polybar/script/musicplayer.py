from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata | sed -n '/title/{n;p}' | cut -d '\"' -f 2")
if my_output == "":
    print('Empty')
else:
    if len(my_output) > 25:
        print(my_output[0:20]+'...')
    else:
        print(my_output)
