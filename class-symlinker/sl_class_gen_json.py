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
        "fzf":          {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"osx"  : "$AB_DLZ_DOTFILES/fzf/.fzf.zsh.osx",
                                                  "arch" : "$AB_DLZ_DOTFILES/fzf/.fzf.zsh.arch"},
                                      "target" : {"all"  : "$HOME/.fzf.zsh"}}]},
        "git-global":   {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/git/.gitignore_global"},
                                      "target" : {"all"  : "$HOME/.gitignore_global"}},
                                     {"source" : {"all"  : "$AB_DLZ_DOTFILES/git/.gitconfig"},
                                      "target" : {"all"  : "$HOME/.gitconfig"}}]},
        "nvim":         {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/nvim/init.lua"},
                                      "target" : {"all"  : "$HOME/.config/nvim/init.lua"}},
                        {"source":  {"all"  : "$AB_DLZ_DOTFILES/nvim/lua"},
                                    "target" : {"all"  : "$HOME/.config/nvim/lua"}}]},
        "powerline":    {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/zsh/.p10k.zsh"},
                                      "target" : {"all"  : "$HOME/.p10k.zsh"}}]},
        "tmux":         {"ostypes": ["arch"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/.tmux.conf"},
                                      "target" : {"arch" : "$HOME/.tmux.conf"}}]},
        "zathura" :     {"ostypes": ["osx", "arch"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/zathura"},
                                      "target" : {"all"  : "$HOME/.config/zathura"}}]},
        "zsh":          {"ostypes": ["arch", "osx"],
                         "paths"  : [{"source" : {"all"  : "$AB_DLZ_DOTFILES/zsh/.bash_profile"},
                                      "target" : {"all"  : "$HOME/.bash_profile"}},
                                     {"source" : {"all"  : "$AB_DLZ_DOTFILES/zsh/.zshrc"},
                                      "target" : {"all"  : "$HOME/.zshrc"}},
                                     {"source" : {"all"  :  "$AB_DLZ_DOTFILES/zsh/.p10k.zsh"},
                                      "target" : {"all"  : "$HOME/.p10k.zsh"}}]},
    }
# }}}1

with open(cwd + '/sl_class_inputs.json', 'w+') as f:
    json.dump(slct , f)
