# -*- coding: utf-8 -*-
{
    'name': "myApp",

    'summary': """
        Short (1  phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        This module adds cards to the partners facilitating the
        operation in the payments
    """,

    'author': "hiregui92",
    'website': "http://www.hiregui92.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Payments',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
    ],

    # always loaded
    'data': [
        # Security
        "security/res_groups.xml",
        # "security/ir.model.access.csv",
        # Data
        'data/card_type.xml',
        'views/partner_card_view.xml',
        'views/res_partner_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    "installable": True,
    "auto_install": False,
}
