# -*- coding: utf-8 -*-

import sys
import os
from odoo import models, fields, api, _
from odoo.exceptions import UserError
try:
    import pyzk
except:
    os.system("pip install pyzk")
sys.path.insert(1, os.path.abspath("./pyzk"))
from zk import ZK, const


class HRAttendance(models.Model):
    _inherit = 'hr.attendance'

    def fetch_attendance_data(self):
        company = self.env.user.company_id
        conn = company.check_zk_connection()
        try:
            # To Make Sure No Activity While Processing This Code
            conn.disable_device()
            attendance_data = conn.get_attendance()
            conn.enable_device()
        except Exception as e:
            print('Something went wrong %s' % e)
        finally:
            if conn:
                conn.disconnect()


