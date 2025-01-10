{
    'name': 'Whatsapp',
    'version': '18.0.1.0.0',
    'category': 'Services',
    'summary': 'Whatsapp Support',
    'description': """
        This module provides support for Whatsapp in Odoo.
    """,
    'author': 'Experts Vision Company',
    'website': 'https://www.expertsvision.com',
    'depends': ['base_accounting_kit'],
    'data': [
        'data/whatsapp_system_parameters.xml'
    ],
    'demo': [],
    'application': False,
    'license': 'AGPL-3',
    # 'images': ['static/description/icon.png'],
    'support': 'support@expertsvision.com',

    # 'installable': True,
    # 'auto_install': False,
    # 'currency': 'EUR',
    # 'maintainer': 'Maintainer Name',
    # 'external_dependencies': {
    #     'python': [],  # Python libraries required
    #     'bin': [],  # External binaries required
    # },
    # 'pre_init_hook': 'pre_init_hook_method',  # Hook to execute before module installation
    # 'post_init_hook': 'post_init_hook_method',  # Hook to execute after module installation
    # 'post_load_hook': 'post_load_hook_method',  # Hook to execute after loading the module
}
