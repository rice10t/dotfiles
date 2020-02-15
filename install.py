from typing import List
import os
from pathlib import Path
import shutil

IDEAVIMRC = Path('.ideavimrc')
TMUX_CONF = Path('.tmux.conf')
INIT_VIM = Path('init.vim')


def is_windows() -> bool:
    return os.name == 'nt'


def expands_to_home(files: List[Path]) -> None:
    for file in files:
        shutil.copy2(str(file), str(Path.home()))


def install(src: Path, target: Path) -> None:
    target.mkdir(exist_ok=True)
    shutil.copy2(str(src), str(target))


def main() -> None:
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
