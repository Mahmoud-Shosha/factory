import logging

from odoo import models

from ..services.whatsapp_service import WhatsappService
from ..services.whatsapp_template import WhatsappTemplate

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    _injection_done = False
    _whatsapp_service = None
    _whatsapp_message_enabled = None

    def __init__(self, env, ids, prefetch_ids):
        super().__init__(env, ids, prefetch_ids)
        if not AccountMove._injection_done:
            AccountMove._whatsapp_service = WhatsappService(self.env)
            AccountMove._injection_done = True

    def action_post(self):
        super(AccountMove, self).action_post()

        whatsapp_message_enabled = self.env['ir.config_parameter'].get_param(
            'invoice_created_whatsapp_message_enabled') == 'True'
        if whatsapp_message_enabled:
            # self.env['account.move'].with_delay().send_whatsapp_message()
            self.__send_whatsapp_message()

    def __send_whatsapp_message(self):
        if not self.partner_id.mobile:
            _logger.info("No Whatsapp message is sent after invoice creation due to missing mobile")
            self.__log_note(False)
            return

        whatsapp_access_token = self.env['ir.config_parameter'].get_param('whatsapp_access_token')
        invoice_id = self.name

        response = self._whatsapp_service.send_whatsapp_message(
            "201228710554",
            WhatsappTemplate.INVOICE_CREATED,
            [{"parameter_name": "invoice_id", "type": "TEXT", "text": invoice_id}],
            [{"parameter_name": "invoice_id", "type": "TEXT", "text": invoice_id}],
            whatsapp_access_token
        )

        self.__log_note(response.status_code == 200)

    def __log_note(self, success):
        if success:
            self.env['mail.message'].create([{
                'subject': 'WhatsApp Notification Sent',
                'body': f"<div class='alert alert-success'>WhatsApp message sent to {self.partner_id.name}</div>",
                'message_type': 'notification',
                'subtype_id': self.env.ref('mail.mt_note').id,
                'model': 'account.move',
                'res_id': self.id,
            }])
        else:
            self.env['mail.message'].create([{
                'subject': 'WhatsApp Notification Failed',
                'body': f"<div class='alert alert-danger'>Failed to send WhatsApp message to {self.partner_id.name or 'Unknown Partner'}</div>",
                'message_type': 'notification',
                'subtype_id': self.env.ref('mail.mt_note').id,
                'model': 'account.move',
                'res_id': self.id,
            }])
