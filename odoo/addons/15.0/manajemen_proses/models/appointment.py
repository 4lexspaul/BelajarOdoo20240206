from odoo import api, fields, models

class ManajemenAppointment(models.Model):
    _name = "manajemen.appointment"
    _description = "Manajemen Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    manajemen_id = fields.Many2one(comodel_name='manajemen.proses', string="Manajemen")
    type = fields.Selection([('high', 'High'), ('middle', 'Middle'), ('low', 'Low')], string='Type', related='manajemen_id.type')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
