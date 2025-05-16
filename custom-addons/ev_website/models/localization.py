from odoo import models, fields, api


class evWebsiteLocalization(models.Model):
    _name = "ev_website.localization"
    _description = "Experts Vision Website Localization"

    name = fields.Char(required=True, unique=True)
    en_value = fields.Char()
    ar_value = fields.Char()
    
    
    # simple retrieval utility function
    @api.model
    def get_translation(self, key, lang='en'):
        record = self.search([('name', '=', key)], limit=1)
        if not record:
            return key  # fallback to the key itself
        return record.en_value if lang == 'en' else record.ar_value