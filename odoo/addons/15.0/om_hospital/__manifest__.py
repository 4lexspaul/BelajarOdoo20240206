# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Manajemen Rumah Sakit',
    'version': '1.0',
    'author : Odoo Pudaks'
    'summary': 'Hospital Management Modul',
    'sequence': -100,
    'description': """Hospital Management Modul""",
    'category': 'Productivity',
    'website': 'http://localhost:8069',
    'license': 'LGPL-3',
    'depends': ['base','sale','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/odoo_playground_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}