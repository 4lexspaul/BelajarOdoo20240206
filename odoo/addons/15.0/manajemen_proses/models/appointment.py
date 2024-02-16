from odoo import api, fields, models

class ManajemenAppointment(models.Model):
    _name = "manajemen.appointment"
    _description = "Manajemen Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'manajemen_id'

    manajemen_id = fields.Many2one(comodel_name='manajemen.proses', string="Manajemen")
    type = fields.Selection([('high', 'High'), ('middle', 'Middle'), ('low', 'Low')], string='Type', related='manajemen_id.type')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='References')
    komentar = fields.Html(string='Komentar', translate=True)

    @api.onchange('manajemen_id')
    def _onchange_manajemen_id(self):
        if self.manajemen_id:
            self.ref = self.manajemen_id.ref
