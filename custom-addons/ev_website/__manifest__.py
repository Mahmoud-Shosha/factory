# -*- coding: utf-8 -*-
{
    'name': "EV_website",

    'summary': "The Website module for EV",

    'description': """
    This module provides a website for the EV project. It includes features such as:
    - Home page
    - Customer page 
    - About us page
    - Contact us page
    - Services page
    """,

    'author': "Kareem",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1', # odoo 18 

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/customers_menu.xml",
        "views/customers.xml",
        "data/about_localization.xml",
        "data/home_localization.xml",
        "data/service_localization.xml",
        "data/header_localization.xml",
        "views/home.xml",
        "views/header.xml",
        "views/services.xml",
        "views/about.xml",
        "views/contact_us.xml",
        "views/contact_thanks.xml",
        "data/contact_localization.xml",
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "assets": {
        "web.assets_common": [
            "/ev_website/static/src/css/styles.css",
        ],
    },
}

