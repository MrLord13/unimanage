from odoo import fields, models, api


class UniManageStudent(models.Model):
    _name = 'unimanage.student'
    _description = 'دانشجو دانشگاه'

    name = fields.Char(string='نام و نام خانوادگی', required=True)
    student_code = fields.Char(string='شماره دانشجویی', required=True, unique=True)
    student_code_meli = fields.Char(string='کد ملی', unique=True)
    student_grade = fields.Char(string='مقطع')
    student_field = fields.Char(string='رشته')
    student_number = fields.Char(string='شماره تماس')
    student_picture = fields.Binary(string='تصویر دانشجو')
    student_description = fields.Text(string='توضیحات دانشجو')
    class_ids = fields.Many2many('unimanage.class', string='کلاس')
    _sql_constraints = [
        ('student_code_meli', 'unique(student_code_meli)', 'این کد ملی وجود دارد'),
        ('student_code', 'unique(student_code)', 'این شماره انشجویی وجود دارد'),
    ]