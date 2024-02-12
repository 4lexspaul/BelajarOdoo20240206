# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _rec_name = 'patient_id'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Database Janji Temu"

    # define many to one id, must end with _id
    patient_id = fields.Many2one(comodel_name="hospital.patient", required=True, tracking=True, string='Nama Pasien')
    date_of_appointment = fields.Date(string='Tanggal Janji Temu', required=True, tracking=True, default=fields.Date.context_today)
    gender = fields.Selection(related='patient_id.gender', string='Jenis Kelamin')
    patient_code = fields.Char(string='Kode Pasien', help='Kode pasien yang digunakan untuk identifikasi pasien')
    active = fields.Boolean(string="Active", default=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default="draft", string="Status", required=True)
    doctor_id = fields.Many2one(comodel_name="res.users", string="Dokter", tracking=True)
    note = fields.Html(string='Catatan')
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string="Pharmacy Lines")
    hide_sales_price = fields.Boolean(string="Hide Sales Price")

    @api.model
    def create(self, vals):
        # print("Helloo buddieess.......!!, self.env['ir.sequence']")
        vals['patient_code'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals)

    # kode ini digunakan jika terdapat sebuah eksisting record, dan recordnya di edit
    # maka akan mengenerat patient_code berdasarkan nomor urut
    def write(self, vals):
        if not self.patient_code:
            vals['patient_code'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).write(vals)

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.patient_code = self.patient_id.patient_code

    def action_test_appointment(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Success !!!!',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', string="Nama Obat", required=True)
    price_unit = fields.Float(related='product_id.lst_price', string="Harga")
    qty = fields.Integer(string="Jumlah")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")