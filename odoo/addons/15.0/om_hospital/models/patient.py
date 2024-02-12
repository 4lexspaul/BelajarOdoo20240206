# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Database Pasien"

    name = fields.Many2one(comodel_name="res.users", required=True, tracking=True, string='Nama Pasien')
    age = fields.Integer('Umur', required=True, tracking=True, compute='_compute_age')
    gender = fields.Selection([
        ('pria', 'Pria'),
        ('wanita', 'Wanita')
    ], required=True, default='other')
    note = fields.Html(string='Catatan')
    active = fields.Boolean(string="Active", default=True)
    date_of_birth = fields.Date(string='Tanggal Lahir', tracking=True)
    patient_code = fields.Char(string='Kode Pasien')
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")
    appointment_count = fields.Integer(string="Appointment Count")

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_('Tanggal Lahir tidak diperbolehkan'))

    @api.model
    def create(self, vals):
        # print("Helloo buddieess.......!!, self.env['ir.sequence']")
        vals['patient_code'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    #kode ini digunakan jika terdapat sebuah eksisting record, dan recordnya di edit
    #maka akan mengenerat patient_code berdasarkan nomor urut
    def write(self, vals):
        if not self.patient_code:
            vals['patient_code'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def name_get(self):
        return [(record.id, "[%s] %s" % (record.patient_code, record.name.display_name))for record in self]
        #patient_list = []
        #for record in self:
            #patient_code = record.patient_code
            #patient_name = record.name.display_name if record.name else ""
            #name = f"{patient_code} {patient_name}"
            #patient_list.append((record.id, name))

        #return [(record.id, "%s:%s" % (record.patient_code, record.name))for record in self]