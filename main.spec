# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
added_files=[('./project/Blastdb','Blastdb'),
('./project/BlastResult','Categories'),
('./project/Categories','BlastResult'),
('./project/Databases','Databases'),
('./project/DbAmbigua','DbAmbigua'),
('./project/FinalResult','FinalResult'),
('./project/Test','Test'),
('./tmp.fa','.')
  ]


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Paula\\PycharmProjects\\Haplotypes'],
             binaries=[],
             datas=added_files,
             hiddenimports=['Bio.SearchIO.BlastIO'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
