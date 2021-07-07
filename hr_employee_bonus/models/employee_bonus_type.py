# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HREmployeeBonusType(models.Model):
    _name = 'hr.employee.bonus.type'
    _description = 'Employee Bonus Types'
    _inherit = 'mail.thread'

    name = fields.Char('Name', required=True)
    calculation_type = fields.Selection([('fixed', 'Fixed Amount'),
                                         ('percentage', 'Percentage'),
                                         ('days', 'Days')], 'Calculation Type', default='fixed', help="""
                                         Fixed Amount : Determined in the process
                                         Percentage : Percentage from the selected salary rule/s
                                         Days : Days amount considering the day amount equals to the sum of the selected salary rule/s divided by the month days 
                                         """, track_visibility='onchange')
    salary_rule_ids = fields.Many2many('hr.salary.rule', string='Salary Rules')
    active = fields.Boolean('Active', default=True, track_visibility='onchange')

    def toggle_active(self):
        # Archive and Unarchive the bonus type
        for rec in self:
            rec.active = not rec.active

    def name_get(self):
        # Modifying The Display Name To Be : Bonus Type Name (Calculation Type)
        res = []
        for rec in self:
            calculation_type_label = dict(self._fields['calculation_type'].selection).get(self.calculation_type)
            res.append((rec.id, rec.name + ' (%s)' % calculation_type_label))
        return res


