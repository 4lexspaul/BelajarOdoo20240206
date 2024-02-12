# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string='Nama Pasien', required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Warna")
    # color_2 = fields.Integer(string="Warna 2")