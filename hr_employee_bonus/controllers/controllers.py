# -*- coding: utf-8 -*-
from odoo import http

# class HrEmployeeBonus(http.Controller):
#     @http.route('/hr_employee_bonus/hr_employee_bonus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employee_bonus/hr_employee_bonus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employee_bonus.listing', {
#             'root': '/hr_employee_bonus/hr_employee_bonus',
#             'objects': http.request.env['hr_employee_bonus.hr_employee_bonus'].search([]),
#         })

#     @http.route('/hr_employee_bonus/hr_employee_bonus/objects/<model("hr_employee_bonus.hr_employee_bonus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employee_bonus.object', {
#             'object': obj
#         })