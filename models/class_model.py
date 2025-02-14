from odoo import models, fields


class UniManageClass(models.Model):
    _name = 'unimanage.class'
    _description = 'کلاس دانشگاه'

    name = fields.Char(string='نام کلاس', required=True)
    class_number = fields.Char(string='شماره کلاس', required=True)
    description = fields.Text(string='توضیحات کلاس')
    session_ids = fields.One2many('unimanage.session', 'class_id', string='جلسات')
    student_ids = fields.Many2many('unimanage.student', string='دانشجویان')