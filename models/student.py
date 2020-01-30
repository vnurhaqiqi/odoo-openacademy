from odoo import fields,api,models
from odoo.exceptions import ValidationError,UserError
import random

class Student(models.Model):
    _name = 'openacademy.student'

    name = fields.Char(string='Name')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    address = fields.Text(string='Address')
    course_id = fields.Many2one('openacademy.course', string='Course')
    total_payment = fields.Float(string='Total Payment', readonly=True, compute='_calculate_payment')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    room_id = fields.Many2one('openacademy.room', string='Room')

    @api.model
    def create(self, vals):
        user_create = super(Student, self).create(vals)
        split_name = user_create.name.lower().split()
        user_name = split_name[0] + str(random.randint(1,201))

        self.env['res.users'].create({
            'name':user_create.name,
            'login':user_name,
            'password':123456
        })

        return user_create

    @api.depends('course_id')
    def _calculate_payment(self):
        for record in self:
            record.total_payment = record.course_id.course_price