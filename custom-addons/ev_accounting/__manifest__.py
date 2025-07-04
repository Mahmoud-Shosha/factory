{
    'name': 'EV Accounting',
    'version': '18.0.1.0.0',
    'category': 'Genral',
    'summary': 'Experts Vision accounting module ',
    'description': """
        This is an accounting module manage the basic accounting workflows
    """,
    'author': 'Experts Vision Company',
    'website': 'https://www.expertsvision.com',

    'depends': [
    # accounting modules 
    'accounting_pdf_reports',
    'om_account_accountant',
    'om_account_asset',
    'om_account_budget',
    'om_account_daily_reports',
    'om_account_followup',
    'om_fiscal_year',
    'om_recurring_payments'
    # note that these modules depend on mail, account
    ],
    'data': [],
    'demo': [],
    'application': False,
    'license': 'AGPL-3',
    'images': ['static/description/icon.png'],
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
