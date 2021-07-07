# -*- coding: utf-8 -*-
{
    'name': "Employee Bonuses",

    'summary': """
        HR Employee Bonuses""",

    'description': """
        Employee Bonuses and the integration with the payroll
    """,

    'author': "Sami Adam",
    'website': "https://www.linkedin.com/in/sami-mohamed-9ab3a598/",
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/employee_bonus_type.xml',
        'views/employee_bonus.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}