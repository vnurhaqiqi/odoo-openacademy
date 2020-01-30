from odoo import fields,api,models
from odoo.exceptions import ValidationError,UserError
from datetime import date

class Session(models.Model):
    _name = 'openacademy.session'

    course_id = fields.Many2one('openacademy.course', string='Course')
    room_id = fields.Many2one('openacademy.room', string='Room')
    student_ids = fields.Many2many('openacademy.student', string='Students')
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')
    state = fields.Selection([('draft','Draft'),('onprogress','On Progress'),('done','Done')], string='State', default='draft')

    @api.model
    def create(self, vals):
        result = super(Session, self).create(vals)

        for student in result.student_ids:
            if student.room_id == False:
                student.write({'room_id':result.room_id.id})
            else:
                raise UserError('Peserta {} sudah memiliki ruangan'.format(student.name))

        return result

    @api.constrains('room_id')
    def _update_room_state(self):
        self.room_id.write({'state':'using'})

    @api.multi
    def btn_onprogress(self):
        self.state = 'onprogress'

    @api.multi
    def btn_done(self):
        self.state = 'done'
        room_obj = self.env['openacademy.room'].search([('id', '=', self.room_id.id)])
        room_obj.write({'state':'done'})