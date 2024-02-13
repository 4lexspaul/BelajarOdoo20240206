from odoo import api, fields, models

class ManajemenProses(models.Model):
    _name = "manajemen.proses"
    _description = "Manajemen Proses"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='References', tracking=True)
    age = fields.Integer(String='Age', tracking=True)
    metode_manpros = fields.Selection([('kuantitatif', 'Kuantitatif'), ('kualitatif', 'Kualitatif')], string="Metode", tracking=True)
    metode_analisis = fields.Selection([('common size financial statement','Common Size Financial Statement'),('index time series','Index Time Series'),('analisis pertumbuhan','Analisis Pertumbuhan'),('analisis industri','Analisis Industri')], string="Metode Analisis", tracking=True)
    type = fields.Selection([('high','High'), ('middle','Middle'), ('low','Low')], string='Type', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)

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