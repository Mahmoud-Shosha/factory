# models/contactus.py

from odoo import models, fields

class ev_customer(models.Model):
    _name = 'ev_website.customer'
    _description = 'Experts vsision contact customers'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email_from = fields.Char(string='Email', required=True)
    company = fields.Char(string='Company')
    subject = fields.Char(string='Subject', required=True)
    description = fields.Text(string='Message', required=True)
