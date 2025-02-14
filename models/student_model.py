from odoo import fields, models, api


class UniManageStudent(models.Model):
    _name = 'unimanage.student'
    _description = 'دانشجو دانشگاه'

    name = fields.Char(string='نام و نام خانوادگی', required=True)
    student_code = fields.Char(string='شماره دانشجویی', required=True, unique=True)
    student_number = fields.Char(string='شماره تماس')
    class_ids = fields.Many2many('unimanage.class', string='کلاس')
