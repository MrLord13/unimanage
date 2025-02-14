from odoo import models, fields


class UniManageClass(models.Model):
    _name = 'unimanage.class'
    _description = 'کلاس دانشگاه'

    name = fields.Char(string='نام کلاس', required=True)
    class_number = fields.Char(string='شماره کلاس', required=True)
    class_capacity = fields.Char(string='ظرفیت کلاس', required=True)
    class_start_date = fields.Char(string='ساعت شروع کلاس')
    class_end_date = fields.Char(string='ساعت پایان کلاس')
    class_exam_date = fields.Char(string='تاریخ امتحان کلاس')
    description = fields.Text(string='توضیحات کلاس')
    session_ids = fields.One2many('unimanage.session', 'class_id', string='جلسات')
    student_ids = fields.Many2many('unimanage.student', string='دانشجویان')