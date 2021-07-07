from odoo import models, fields, api, _
from odoo.exceptions import UserError
import os
import sys
try:
    import pyzk
except:
    os.system("pip install pyzk")
sys.path.insert(1, os.path.abspath("./pyzk"))
from zk import ZK, const


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    zk_device_ip = fields.Char('ZK Device IP')
    zk_device_port = fields.Integer('ZK Device Port', default=4370)
    connection_timeout = fields.Integer('Connection Timeout', default=5)

    def check_zk_connection(self):
        self.env.user.company_id.check_zk_connection()

    @api.model
    def create(self, vals):
        res = super(ResConfigSettings, self).create(vals)
        company = self.env.user.company_id
        if 'zk_device_ip' in vals:
            company.write({'zk_device_ip': vals['zk_device_ip']})
        if 'zk_device_port' in vals:
            company.write({'zk_device_port': vals['zk_device_port']})
        if 'connection_timeout' in vals:
            company.write({'connection_timeout': vals['connection_timeout']})
        return res

    @api.multi
    def write(self, vals):
        company = self.env.user.company_id
        res = super(ResConfigSettings, self).write(vals)
        for rec in self:
            zk_device_ip = rec.zk_device_ip
            zk_device_port = rec.zk_device_port
            connection_timeout = rec.connection_timeout
            if 'zk_device_ip' in vals:
                zk_device_ip = vals['zk_device_ip']
            if 'zk_device_port' in vals:
                zk_device_port = vals['zk_device_port']
            if 'connection_timeout' in vals:
                connection_timeout = vals['connection_timeout']
            company.write(
                {'zk_device_ip': zk_device_ip,
                 'zk_device_port': zk_device_port,
                 'connection_timeout': connection_timeout})
        return res

    @api.model
    def default_get(self, fields):
        res = super(ResConfigSettings, self).default_get(fields)
        company = self.env.user.company_id
        zk_device_ip = company.zk_device_ip
        zk_device_port = company.zk_device_port
        connection_timeout = company.connection_timeout
        res.update({'zk_device_ip': zk_device_ip,
                    'zk_device_port': zk_device_port,
                    'connection_timeout': connection_timeout})
        return res


class ResCompany(models.Model):
    _inherit = 'res.company'

    zk_device_ip = fields.Char('ZK Device IP')
    zk_device_port = fields.Integer('ZK Device Port', default=4370)
    connection_timeout = fields.Integer('Connection Timeout', default=5)

    def check_zk_connection(self):
        ip = self.zk_device_ip  # ZK Device IP Address
        port = self.zk_device_port  # ZK Device Connection Port
        connection_timeout = self.connection_timeout
        zk = ZK(ip, port=port, timeout=connection_timeout, password=0,
                      force_udp=False, ommit_ping=False)
        try:
            conn = zk.connect()
            return conn
        except Exception as e:
            raise UserError(e)
