# -*- coding: utf-8 -*-
{
    'name': "Attendance ZKteco",

    'summary': """
        HR Attendance and ZKteco biometrics integration""",

    'description': """
        A module for ZKteco biometrics integration, allowing you to fetch attendance data from 
        ZKteco devices.
    """,

    'author': "Sami Adam",
    'website': "https://www.linkedin.com/in/sami-mohamed-9ab3a598/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/settings.xml',
        'views/hr_attendance_zk.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}