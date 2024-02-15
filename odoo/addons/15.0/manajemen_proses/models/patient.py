from datetime import date
from odoo import api, fields, models

class ManajemenProses(models.Model):
    _name = "manajemen.proses"
    _description = "Manajemen Proses"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='References', tracking=True)
    age = fields.Integer(String='Age', compute='_compute_age', tracking=True)
    metode_manpros = fields.Selection([('kuantitatif', 'Kuantitatif'), ('kualitatif', 'Kualitatif')], string="Metode", tracking=True, default='kuantitatif')
    metode_analisis = fields.Selection([('common size financial statement','Common Size Financial Statement'),('index time series','Index Time Series'),('analisis pertumbuhan','Analisis Pertumbuhan'),('analisis industri','Analisis Industri')], string="Metode Analisis", tracking=True)
    type = fields.Selection([('high','High'), ('middle','Middle'), ('low','Low')], string='Type', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in sefl:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

#    name = fields.Char(string='Account', required=True, translate=True)
#    include_initial_balance = fields.Boolean(string="Bring Accounts Balance Forward", help="Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.")
#    type = fields.Selection([
#        ('other', 'Regular'),
#        ('receivable', 'Receivable'),
#        ('payable', 'Payable'),
#        ('liquidity', 'Liquidity'),
#    ], required=True, default='other',
#        help="The 'Internal Type' is used for features available on "\
#        "different types of accounts: liquidity type is for cash or bank accounts"\
#        ", payable/receivable is for vendor/customer accounts.")