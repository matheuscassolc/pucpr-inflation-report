from typing import Any

from aws import AmazonWebServices


class SimpleEmailService(AmazonWebServices):
    @property
    def resource_name(self) -> str:
        return "ses"

    def send_email(self, **email_params) -> Any:
        self.client.send_email(**email_params)
