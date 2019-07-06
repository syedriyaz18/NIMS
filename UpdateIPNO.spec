# -*- mode: python -*-
a = Analysis(['UpdateIPNO.py'],
             pathex=['C:\\Python27\\ShahiSolutions'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='UpdateIPNO.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='logo.ico')
