# -*- coding: utf-8 -*-
from odoo import http
import logging

_logger = logging.getLogger(__name__)


class EvWebsite(http.Controller):

    def _get_website(self):
        website = http.request.env["website"].get_current_website()
        if not website:
            _logger.warning(
                "No current website found, falling back to any available website."
            )
            website = http.request.env["website"].sudo().search([], limit=1)
        return website

    def _get_translation(self):
        locale = http.request.lang.iso_code  # e.g., 'ar', 'en'
        def _t(key):
            record = http.request.env['ev_website.localization'].sudo().search([('name', '=', key)], limit=1)
            return getattr(record, f'{locale}_value', key) or key
        return _t

    def _render_page(self, template):
        return http.request.render(
            template,
            {
                "name": "EV Website",
                "website": self._get_website(),
                "t": self._get_translation()
            },
        )

    @http.route("/EV", auth="public", website=True)
    def index(self, **kw):
        return self._render_page("ev_website.homepage_template")

    @http.route("/services", auth="public", website=True)
    def services(self, **kw):
        return self._render_page("ev_website.services_template")
    @http.route("/about", auth="public", website=True)
    def about(self, **kw):
        return self._render_page("ev_website.about_template")
    @http.route("/contactus", auth="public", website=True)
    def contact_us(self, **kw):
        return self._render_page("ev_website.contact_us_template")    
    @http.route("/contactus-thank-you", auth="public", website=True)
    def contact_us_thank(self, **kw):
        _logger.info("Received query parameters: %s", kw)

        # Extract values safely
        name = kw.get('name')
        phone = kw.get('phone')
        email_from = kw.get('email_from')
        company = kw.get('company')
        subject = kw.get('subject')
        description = kw.get('description')

        # Create customer record if data is valid
        customer = None
        if name and email_from and subject and description:
            customer = http.request.env['ev_website.customer'].sudo().create({
                'name': name,
                'email_from': email_from,
                'phone': phone,
                'description': description,
                'company': company,
                'subject': subject,
            })
            _logger.info("Customer record created with ID: %s", customer.id)
        else:
            _logger.warning("Insufficient data to create customer")

        return self._render_page("ev_website.contact_us_thanks_template")
    