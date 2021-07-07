# -*- coding: utf-8 -*-
from odoo import http

# class HrAttendanceZkteco(http.Controller):
#     @http.route('/hr_attendance_zkteco/hr_attendance_zkteco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_attendance_zkteco/hr_attendance_zkteco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_attendance_zkteco.listing', {
#             'root': '/hr_attendance_zkteco/hr_attendance_zkteco',
#             'objects': http.request.env['hr_attendance_zkteco.hr_attendance_zkteco'].search([]),
#         })

#     @http.route('/hr_attendance_zkteco/hr_attendance_zkteco/objects/<model("hr_attendance_zkteco.hr_attendance_zkteco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_attendance_zkteco.object', {
#             'object': obj
#         })