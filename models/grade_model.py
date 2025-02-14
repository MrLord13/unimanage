from odoo import fields, models, api


class UniManageGrade(models.Model):
    _name = 'unimanage.grade'
    _description = 'نمره'

    assignment_id = fields.Many2one('unimanage.assignment', string='تکلیف')
    student_id = fields.Many2one('unimanage.student', string='دانشجو')
    score = fields.Float(string='نمره')
