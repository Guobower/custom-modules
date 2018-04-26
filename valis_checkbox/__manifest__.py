# -*- coding: utf-8 -*-
{
    'name': "Valis Checkbox",

    'summary': """
        Checkbox for tasks""",

    'description': """
        Checkbox for tasks
    """,

    'author': "Valis",
    'website': "http://valis.kz",

    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/valis_checkbox_views.xml',
    ],
}
