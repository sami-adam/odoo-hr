# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, date
import calendar


class HREmployeeBonus(models.Model):
    _name = 'hr.employee.bonus'
    _description = 'Employee Bonuses'
    _inherit = 'mail.thread'

    name = fields.Char('Description')
    date = fields.Date('Date', default=fields.Date.context_today)
    date_confirm = fields.Date('Confirmation Date', track_visibility='onchange')
    employee_id = fields.Many2one('hr.employee', 'Employee')
    department_id = fields.Many2one(related='employee_id.department_id', string='Department', help='Employee Department')
    job_id = fields.Many2one(related='employee_id.job_id', string='Job Position', help='Employee Job Position')
    bonus_type_id = fields.Many2one('hr.employee.bonus.type', 'Bonus Type')
    calculation_type = fields.Selection(related='bonus_type_id.calculation_type', string='Calculation Type')
    amount_percentage = fields.Float(help="""
    In case of fixed amount, bonus amount = Amount * Quantity
    In case of percentage, bonus amount = (The sum of the salary rule/s amount * Percentage /100) * Quantity
    In Case of days, bonus amount = (Day Amount * Percentage /100) * Quantity
    """)
    quantity = fields.Float('Quantity', default=1)
    bonus_amount = fields.Float('Bonus Amount')  # Todo Add Currency Sign To The Amount
    note = fields.Text('Notes')
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.user.company_id.currency_id)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('paid', 'Paid'),
                              ('cancelled', 'Cancelled')], track_visibility='onchange', default='draft')

    def action_confirm(self):
        # Calculate bonus amount and confirm the request
        if not self.employee_id.contract_id:
            raise UserError(_('Please Make Sure The Selected Employee Has Valid Contract'))
        bonus_amount = 0.0
        if self.calculation_type in ['percentage', 'days']:
            date_today = date.today()
            month_days = calendar.monthrange(date_today.year, date_today.month)[1]
            salary_rule_obj = self.env['hr.salary.rule']
            rules_amount = 0
            for rule in self.bonus_type_id.salary_rule_ids:
                try:
                    rules_amount += salary_rule_obj.get_rule_amount(rule, self.employee_id)
                except Exception as e:
                    raise UserError(e)
            if self.calculation_type == 'percentage':
                bonus_amount = rules_amount * (self.amount_percentage / 100) * self.quantity
            elif self.calculation_type == 'days':
                bonus_amount = (rules_amount / month_days) * (self.amount_percentage / 100) * self.quantity
        else:
            bonus_amount = self.amount_percentage * self.quantity
        self.write({'bonus_amount': bonus_amount, 'state': 'confirmed', 'date_confirm': date_today})

    def action_cancel(self):
        if self.sate == 'confirmed':
            self.state = 'cancelled'
        else:
            raise UserError(_('Sorry! Only Confirmed Requests Can Be Cancelled'))

    def action_draft(self):
        if self.state == 'cancelled':
            self.state = 'draft'
        else:
            raise UserError(_('Sorry! Only Cancelled Request Can Be Set To Draft'))






