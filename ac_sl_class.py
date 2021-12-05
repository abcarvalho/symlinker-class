# %%
import sys
import os

import json

fpath = os.path.realpath(__file__)
cwd = os.path.dirname(fpath)

class SLObj():
    # defining constructor
    def __init__(self):
        self._ostype = ostype = 'osx' if os.uname().sysname == 'Darwin' else "arch"
        self = self.get_config_data()

    def sl_check_avail(self, app: str, ostype: str):
        if (ostype not in ['osx', 'arch']):
            print("Error! OS Type not recognized. Exiting...")
            return False
        elif app not in self.data.keys():
            print("Error! App config files not available. Exiting...")
            return False
        else:
            cond = ostype in self.data[app]["ostypes"]
            for x in self.data[app]["paths"]:
                skeys = x["source"].keys()
                tkeys = x["target"].keys()
                # source condition
                cond = cond & ((ostype in skeys) | ("all" in skeys))
                # target condition
                cond = cond & ((ostype in tkeys) | ("all" in tkeys))

            return cond

    # List of Apps with Config Available for the OS Type:
    def get_os_apps(self, ostype: str):
        if (ostype not in ['osx', 'arch']):
            print("Error! OS Type not recognized. Exiting...")
        else:
            return [x for x in self.data.keys() if self.sl_check_avail(x, ostype)]

    def get_config_data(self):
        # update list of config files and directories:
        os.system('python ' + cwd + "/sl_class_gen_json.py")

        # import data
        f = open(cwd + '/sl_class_inputs.json',)
        self.data = json.load(f)
        f.close()

        # set lists of OS-specific apps
        self.osx_apps = self.get_os_apps("osx")
        self.arch_apps = self.get_os_apps("arch")

    # List of Apps with Config Available for the OS Type
    # AND Market for Installation:
    def get_os_apps_install(self):
        app_list = self.get_os_apps(self._ostype)
        return [x for x in app_list if (self._ostype in self.data[x]["ostypes"])]

    # List of Apps with Config Available for the OS Type
    # AND NOT Market for Installation:
    def get_os_apps_not_install(self):
        app_list = self.get_os_apps(self._ostype)
        excl_apps = [x for x in app_list if (self._ostype not in self.data[x]["ostypes"])]

        if excl_apps:
            print("Apps not marked for installation: ")
            for x in excl_apps:
                print("- " + x)

        return excl_apps

    # List of Apps Marked for Installation
    # BUT without Config Available for the OS Type:
    def get_os_apps_missing_paths(self):
        apps_2_install = [x for x in self.data.keys()
                          if (self._ostype in self.data[x]["ostypes"])]
        app_list = self.get_os_apps(self._ostype)
        amp = [x for x in apps_2_install if (x not in app_list)]
        if amp:
            print("Apps marked for installation but missing paths: ")
            for x in amp:
                print("- " + x)

    # Generate Full Paths by Reading Shell Variables:
    def get_os_path(self, x: str):
        shell_var = str.split(x, "/")[0][1:]
        remainder = "/".join(str.split(x, "/")[1:])
        return os.environ[shell_var] + "/" + remainder

    def symlinker_core(self, source: str, target: str,
                          replace: bool = True):
        print("Source: " + source)
        print("Target: " + target)

        target_exists = (os.path.isfile(self.get_os_path(target)) |
                         os.path.isdir(self.get_os_path(target))  |
                         os.path.islink(self.get_os_path(target)))

        tmsg = "Target already exists!"
        if target_exists:
            if replace:
                print(tmsg + " -> " + "Will force symlink! \n")

                print("Removing previous object...")
                os.system('rm -rf ' + target)
            else:
                print(tmsg + "-> Skipping...")
                return

        print("Symlinking object...")
        os.symlink(self.get_os_path(source), self.get_os_path(target))

    def symlinker(self, app: str, replace: bool = False):
        if self.sl_check_avail(app, self._ostype):
            if self._ostype not in self.data[app]["ostypes"]:
                print("WARNING: App " + app + " not marked to be installed in OS " + self._ostype + "!")
                print("Skipping... ")
            else:
                for x in self.data[app]["paths"]:
                    source = x["source"][self._ostype] if self._ostype in x["source"].keys() else x["source"]["all"]
                    target = x["target"][self._ostype] if self._ostype in x["target"].keys() else x["target"]["all"]
                    self.symlinker_core(source, target, replace=replace)
            print(" ")
