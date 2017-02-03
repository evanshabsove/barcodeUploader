# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/evanshabsove/Documents/barcodeGenerator/app'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('BADGE DESIGN.png', '/home/evanshabsove/Documents/barcodeGenerator/app/BADGE DESIGN.png', 'DATA')]
a.datas += [('Databased.csv', '/home/evanshabsove/Documents/barcodeGenerator/app/Databased.csv', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
