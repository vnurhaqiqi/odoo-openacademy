from odoo import fields,api,models
from odoo.exceptions import ValidationError,UserError

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string='Course Name')
    course_type = fields.Selection([('parttime', 'Part Time Course'),('fulltime','Full Time Course')], string='Course Type')
    course_lv = fields.Selection([('beginner','Beginner'),('intermediate', 'Intermediate'),('advance','Advance')], string='Course Level')
    course_price = fields.Float(string='Price')
    description = fields.Html(string='Course Description')
    instructor_ids = fields.Many2many('openacademy.instructor', string='Instructors')
    capacity = fields.Float(string='Capacity')
    # room_ids = fields.Many2many('openacademy.room', string='Rooms')

class Instructor(models.Model):
    _name = 'openacademy.instructor'

    name = fields.Char(string='Name')
    dob = fields.Date(string='Date of Birth')
    related_field = fields.Char(string='Related Field')

class Room(models.Model):
    _name = 'openacademy.room'

    name = fields.Char(string='Room Number')
    state = fields.Selection([('available','Available'), ('using','Using'), ('done','Done')], string='State', default='available')
    # room_size = fields.Integer(string='Room Size')