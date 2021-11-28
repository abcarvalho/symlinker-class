import os
import json

fpath = os.path.realpath(__file__)
cwd = os.path.dirname(fpath)

slct = {"conda":        {"ostypes": ["osx"],
                         "paths": [{"source": {"all": "$AB_DLZ_DOTFILES/.condarc"},
                                      "target": {"osx": "$HOME/.condarc"}}]},
        "digikam":      {"ostypes": ["osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/digikamrc"},
                                      "target" : {"osx"  : "$HOME/Library/Preferences/digikamrc"}}]},
        "doom":         {"ostypes": ["osx"],
                         "paths"  : [{"source" : {"osx"  : "$AB_DLZ_DOTFILES/.doom.d"},
                                      "target" : {"osx"  : "$HOME/.doom.d"}}]},
        "feh":          {"ostypes": ["arch"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/.fehbg"},
                                      "target" : {"arch" : "$HOME/.fehbg"}}]},
        "fzf":          {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"osx"  : "$AB_DLZ_DOTFILES/fzf/.fzf.zsh.osx",
                                                  "arch" : "$AB_DLZ_DOTFILES/fzf/.fzf.zsh.arch"},
                                      "target" : {"all"  : "$HOME/.fzf.zsh"}}]},
        "git-global":   {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/git/.gitignore_global"},
                                      "target" : {"all"  : "$HOME/.gitignore_global"}},
                                     {"source" : {"all"  : "$AB_DLZ_DOTFILES/git/.gitconfig"},
                                      "target" : {"all"  : "$HOME/.gitconfig"}}]},
        "jrnl":         {"ostypes": [],
                         "paths"  : [{"source" : {"osx"  : "$AB_DLZ_DOTFILES/jrnl"},
                                      "target" : {"osx"  : "$HOME/.config/jrnl"}}]},
        "newsboat":     {"ostypes": [],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/.newsboat/config"},
                                      "target" : {"osx"  : "$HOME/.newsboat/config"}},
                                     {"source" : {"all"  : "$AB_DLZ_DOTFILES/.newsboat/urls"},
                                      "target" : {"osx"  : "$HOME/.newsboat/urls"}}]},
        "nvim":         {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/nvim/init.lua"},
                                      "target" : {"all"  : "$HOME/.config/nvim/init.lua"}},
                        {"source":  {"all"  : "$AB_DLZ_DOTFILES/nvim/lua"},
                                    "target" : {"all"  : "$HOME/.config/nvim/lua"}}]},
        "powerline":    {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/zsh/.p10k.zsh"},
                                      "target" : {"all"  : "$HOME/.p10k.zsh"}}]},
        "ranger":       {"ostypes": [],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/rc.conf"},
                                      "target" : {"all"  : "$HOME/.config/ranger/rc.conf"}}]},
        "sc-im":       {"ostypes":  [],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/sc-im"},
                                      "target" : {"all"  : "$HOME/.config/sc-im"}}]},
        "sxhkd":        {"ostypes": ["arch"],
                         "paths"  : [{"source" : {"arch"  : "$AB_DLZ_DOTFILES/sxhkd"},
                                      "target" : {"arch"  : "$HOME/.config/sxhkd"}}]},
        "systemd":      {"ostypes": ["arch"],
                         "paths"  : [{"source" : {"arch"  : "$AB_DLZ_DOTFILES/systemd"},
                                      "target" : {"arch"  : "$HOME/.config/systemd"}}]},
        "taskwarrior":  {"ostypes": [],
                         "paths"  : [{"source" : {"osx"  : "$AB_DLZ_DOTFILES/.taskrc"},
                                      "target" : {"osx"  : "$HOME/.taskrc"}}]},
        "taskopen":     {"ostypes": [],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/.taskopenrc"},
                                      "target" : {"all"  : "$HOME/.taskopenrc"}}]},
        "timewarrior":  {"ostypes": [],
                         "paths"  : [{"source" : {"osx"  : "$AB_WIKI_DIR/.timewarrior"},
                                      "target" : {"osx"  : "$HOME/.timewarrior"}}]},
        "tig":          {"ostypes": [],
                         "paths"  : [{"source" : {"osx"  : "$AB_DLZ_DOTFILES/tig"},
                                      "target" : {"osx"  : "$HOME/.config/tig"}}]},
        "tmux":         {"ostypes": ["arch"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/.tmux.conf"},
                                      "target" : {"arch" : "$HOME/.tmux.conf"}}]},
        "todo.txt":     {"ostypes": ["osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/todo.txt/.todo.cfg"},
                                      "target" : {"osx" : "$HOME/.todo.cfg"}}]},
        "vit":          {"ostypes": [],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/.vit"},
                                      "target" : {"all" : "$HOME/.vit"}}]},
        "vscode":       {"ostypes": [],
                         "paths"  : [{"source" : {"osx" : "$AB_DLZ_DOTFILES/vscode/settings.json"},
                                      "target" : {"osx" : "$HOME/Library/Application Support/Code/User/settings.json"}},
                                     {"source" : {"osx" : "$AB_DLZ_DOTFILES/vscode/keybidings.json"},
                                      "target" : {"osx" : "$HOME/Library/Application Support/Code/User/keybidings.json"}}]},
        "xinit":        {"ostypes": ["arch"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/.xinitrc"},
                                      "target" : {"arch" : "$HOME/.xinitrc"}}]},
        "zathura" :     {"ostypes": ["osx", "arch"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/zathura"},
                                      "target" : {"all"  : "$HOME/.config/zathura"}}]},
        "zsh":          {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/zsh/.zshrc"},
                                      "target" : {"all"  : "$HOME/.zshrc"}},
                                     {"source" : {"all"  :  "$AB_DLZ_DOTFILES/zsh/.p10k.zsh"},
                                      "target" : {"all"  : "$HOME/.p10k.zsh"}}]},
    }
# }}}1

with open(cwd + '/sl_class_inputs.json', 'w+') as f:
    json.dump(slct , f)
