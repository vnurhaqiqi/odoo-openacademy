from odoo import fields,api,models
from odoo.exceptions import ValidationError
from datetime import datetime

class SessionReportWizard(models.TransientModel):
    _name = 'openacademy.session.report.wizard'

    date_start = fields.Date(string='Date Start', required=True)
    date_end = fields.Date(string='Date End', required=True)

    @api.multi
    def get_report(self):
        data = {
            'ids':self.ids,
            'model':self._name,
            'form':{
                'date_start':self.date_start,
                'date_end':self.date_end,
            }
        }

        return self.env.ref('openacademy.session_report').report_action(self, data=data)

class ReportSession(models.AbstractModel):
    _name = 'report.openacademy.session_report_template_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']

        data = []
        sessions = self.env['openacademy.session'].search([('date_start', '>=', date_start),('date_end', '<=', date_end)])


        return {
            'doc_ids':data['ids'],
            'doc_model':data['model'],
        }