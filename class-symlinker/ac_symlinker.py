# Modules {{{1
import sys
import os

# Get current working directory
wkdir = os.environ["AB_DLZ_DOTFILES"] + "/class-symlinker"
sys.path.append(wkdir)
from ac_sl_class import SLObj

app = str(sys.argv[1])                                             # get app name
replace = int(sys.argv[2]) == 1 if len(sys.argv) > 2 else False    # replace if object exists?
                               # operating system
sl = SLObj()
print("OS Type: " + sl._ostype)
print("Replace if file exists? " + str(replace))

if app == 'all':
    val = ''
    while val not in ['y', 'yes', 'n', 'no']:
        val = input("Symlink all apps? (y/n): ")
        if val not in ['y', 'yes', 'n', 'no']:
            print("Input not understood. Please enter 'y' or 'n'.")

    if val in ['y', 'yes']:
        for app in sl.get_os_apps(sl._ostype):
            sl.symlinker(app, replace=replace)
    else:
        print("Exiting...")
        quit()
else:
    sl.symlinker(app, replace=replace)
