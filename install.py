import os
from pathlib import Path
import shutil

if os.name == 'nt':
    dotfiles = ['.ideavimrc']
    for file in dotfiles:
        shutil.copy2(file, str(Path.home()))

    # Neovim
    nvim_path = Path(os.environ['LOCALAPPDATA'], 'nvim')
    nvim_path.mkdir(exist_ok=True)
    shutil.copy2('init.vim', str(nvim_path))

else:
    dotfiles = ['.ideavimrc', '.tmux.conf']
    for file in dotfiles:
        print(Path.home())
        Path.home().symlink_to(file)

    # Neovim
