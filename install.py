import os
from pathlib import Path
import shutil

IDEAVIMRC = '.ideavimrc'
TMUX_CONF = '.tmux.conf'
INIT_VIM = 'init.vim'


def is_windows():
    return os.name == 'nt'


def expands_to_home(files):
    for file in files:
        shutil.copy2(file, str(Path.home()))


def install(src, target):
    target.mkdir(exist_ok=True)
    shutil.copy2(src, str(target))


def main():
    if is_windows():
        dotfiles = [IDEAVIMRC]
        expands_to_home(dotfiles)
    else:
        dotfiles = [IDEAVIMRC, TMUX_CONF]
        expands_to_home(dotfiles)

    # Neovim
    if is_windows():
        nvim_path = Path(os.environ['LOCALAPPDATA'], 'nvim')
        install(INIT_VIM, nvim_path)
    else:
        nvim_path = Path.home() / '.config' / 'nvim'
        install(INIT_VIM, nvim_path)


main()
