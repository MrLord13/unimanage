from odoo import fields, models, api


class UniManageSession(models.Model):
    _name = 'unimanage.session'
    _description = 'جلسات دانشگاه'

    name = fields.Char(string='جلسه', required=True)
    date = fields.Date(string='تاریخ', required=True)
    class_id = fields.Many2one('unimanage.class', string='کلاس')
    material = fields.Text(string='خلاصه محتوا')
    file = fields.Binary(string='فایل پیوست')
    assignment_ids = fields.One2many('unimanage.assignment', 'session_id', string='تکالیف')
