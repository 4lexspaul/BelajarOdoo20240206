from datetime import date
from odoo import api, fields, models

class ManajemenProses(models.Model):
    _name = "manajemen.proses"
    _description = "Manajemen Proses"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='References', tracking=True)
    age = fields.Integer(String='Age', compute='_compute_age', tracking=True, store=True)
    metode_manpros = fields.Selection([('kuantitatif', 'Kuantitatif'), ('kualitatif', 'Kualitatif')], string="Metode", tracking=True, default='kuantitatif')
    metode_analisis = fields.Selection([('common size financial statement','Common Size Financial Statement'),('index time series','Index Time Series'),('analisis pertumbuhan','Analisis Pertumbuhan'),('analisis industri','Analisis Industri')], string="Metode Analisis", tracking=True)
    type = fields.Selection([('high','High'), ('middle','Middle'), ('low','Low')], string='Type', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    appointment_id = fields.Many2one('manajemen.appointment', string="Appointment")


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1