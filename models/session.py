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
            student.write({'room_id':result.room_id.id})

        result.room_id.write({'state':'using'})

        return result

    @api.multi
    def btn_onprogress(self):
        for record in self:
            record.state = 'onprogress'

    @api.multi
    def btn_done(self):
        for record in self:
            record.state = 'done'
            room_obj = self.env['openacademy.room'].search([('id', '=', record.room_id.id)])
            room_obj.write({'state':'done'})

    @api.constrains('student_ids')
    def _check_student_course_room(self):
        for student in self.student_ids:
            if student.room_id != False:
                raise UserError('Peserta {} sudah memiliki ruangan'.format(student.name))