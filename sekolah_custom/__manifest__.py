{
    'name': 'Sekolah Custom',
    'version': '12.0.0.0.0',
    'summary': 'aplikasi sekolah custom',
    'author': "Mplus Software, Odoo Community Association (OCA)",
    'license': "LGPL-3",
    'category': 'base',
    'website': "http://mplus.software/",
    'depends': ["sekolah"],
    'data': [
        'security/ir.model.access.csv',
    	'views/ekstrakul_view.xml',
        'views/trainer_view.xml',
        'views/evaluasi_view.xml',
        'views/evaluasi_det_view.xml',
        'wizard/generate_evaluasi_wizard_view.xml',
        'wizard/tambah_ekskul_wizard_view.xml',
        'reports/report_trainer.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}

