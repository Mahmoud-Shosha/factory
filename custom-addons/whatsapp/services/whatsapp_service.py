import logging

import requests

_logger = logging.getLogger(__name__)


class WhatsappService:

    def __init__(self, env):
        self.env = env
        self.send_url = "https://graph.facebook.com/v21.0/502958002906907/messages"

    def send_whatsapp_message(self, to_number, template, template_header_parameters, template_body_parameters,
                              whatsapp_access_token):
        headers = self.__build_headers(whatsapp_access_token)
        payload = self.__build_payload(to_number, template, template_header_parameters, template_body_parameters)

        response = requests.post(url=self.send_url, headers=headers, json=payload)

        _logger.info(response.json())

        return response

    def __build_headers(self, whatsapp_access_token):
        return {
            "Authorization": f"Bearer {whatsapp_access_token}",
            "Content-Type": "application/json"
        }

    def __build_payload(self, to_number, template, template_header_parameters, template_body_parameters):
        return {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "template",
            "template": {
                "name": template.value,
                "language": {"code": "en_US"},
                "components": [
                    {"type": "header", "parameters": template_header_parameters},
                    {"type": "body", "parameters": template_body_parameters}
                ]
            }
        }
