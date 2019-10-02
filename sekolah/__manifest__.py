{
    'name': 'Sekolah',
    'version': '12.0.0.0.0',
    'summary': 'aplikasi sekolah',
    'author': "Mplus Software, Odoo Community Association (OCA)",
    'license': "LGPL-3",
    'category': 'base',
    'website': "http://mplus.software/",
    'depends': [],
    'data': [
      'security/ir.model.access.csv',
      'views/t_ujian_det_view.xml',
      'views/t_ujian_view.xml',
      'views/mata_pelajaran_view.xml',
      'views/siswa_view.xml',
      'views/main_menu.xml',
      'wizard/ubah_kelas_wizard_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}