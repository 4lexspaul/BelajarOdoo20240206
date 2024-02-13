from odoo import api, fields, models

class ManajemenProses(models.Model):
    _name = "manajemen.appointment"
    _description = "Manajemen Proses"
    _inherit = ['mail.thread', 'mail.activity.mixin']

