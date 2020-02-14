import os

if os.name == 'nt':
    print(os.environ['LOCALAPPDATA'])

    try:
        nvim_dir = os.path.join(os.environ['LOCALAPPDATA'], 'nvim')
        if not os.path.exists(nvim_dir):
            os.mkdir(nvim_dir)
        os.symlink('init.vim', nvim_dir)
        print('ok')
    except PermissionError as e:
        print('PermissionError: ', e)
    except OSError as e:
        print('OSError: ', e)
        print('シンボリックリンクを作成するためには、 Windows 10 のデベロッパーモードを有効にするか、スクリプトを管理者として実行する必要があります。')
        # print('You need to enable Developer Mode for Windows or the process must be run as an administrator.')
else:
    pass
