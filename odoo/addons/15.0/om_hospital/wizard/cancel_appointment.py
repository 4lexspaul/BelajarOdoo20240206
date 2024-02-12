# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Mreport_actionany2one('hospital.appointment', string='Janji Temu')
                                     #domain=[('state', '=', 'draft'), ('priority', 'in', ('0', '1', False))])
    reason = fields.Text(string='Alasan')
    date_cancel = fields.Date(string='Tanggal Cancel')


    def action_cancel_appointment(self):
        if self.appointment_id.date_of_appointment == fields.Date.today():
            raise ValidationError(_('Tanggal cancel tidak boleh sama dengan tanggal janji temu'))
        return {'type': 'ir.actions.act_window_close'}