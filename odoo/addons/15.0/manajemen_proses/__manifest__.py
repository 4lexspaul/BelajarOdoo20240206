# -*- coding: utf-8 -*-

{
    'name': 'Manajemen Proses',
    'version': '1.0.0',
    'category': 'Manajemen',
    'author': 'Odoo PS',
    'sequence': -100,
    'summary': 'Manajemen Proses Sistem',
    'description': """Manajemen Proses Sistem""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/manpros_view.xml',
        'views/analisis_review_view.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3'
}
