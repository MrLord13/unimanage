from odoo import fields, models, api


class UniManageAssignment(models.Model):
    _name = 'unimanage.assignment'
    _description = 'تکالیف'

    name = fields.Char(string='تکلیف', required=True)
    due_date = fields.Date(string='تاریخ انقضاء', required=True)
    session_id = fields.Many2one('unimanage.session', string='جلسه')
    student_ids = fields.Many2many('unimanage.student', string='انجام دهنده ها')
    grade_ids = fields.One2many('unimanage.grade', 'assignment_id', string='نمره')
