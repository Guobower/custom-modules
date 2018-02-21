# -*- coding: utf-8 -*-
{
    'name': "Valis Project",

    'summary': """
        Custom Project Module""",

    'description': """
        Custom project
    """,

    'author': "Valis",
    'website': "http://valis.kz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'views/valis_project_views.xml',
    ],
}
