import json
from typing import Any, Dict, List
from datetime import datetime

import pandas as pd

from inflation_report.src.aws import SimpleEmailService as ses
from inflation_report.src.aws import SimpleNotificationService as sns
from inflation_report.src.report import InflationReporter

from templates import inflation_report_email


class Handler:
    def __init__(self) -> None:
        self.source_email: str = "cassol.matheus@pucpr.edu.br"

        self.now: datetime.datetime = datetime.now()
        self.now_date: "datetime.date" = self.now.strftime("%Y-%m-%d")

    def _get_inflation_report(self) -> pd.DataFrame:
        return InflationReporter(self.now_date).generate_report()

    def _get_inflation_summary(self, inflation_report: pd.DataFrame) -> Dict[str, Any]:
        return inflation_report.to_dict()

    def _generate_html_email_message(self, inflation_summary: Dict[str, Any]) -> str:
        report_message: str = (
            f"O Departamento de Economia da PUCPR informa que a inflação do mês {self.now.month()}"
            f" foi de {inflation_summary.get(inflation_rate)}%"
        )
        html_email_message: str = inflation_report_email.replace("__MESSAGE__", report_message)
        return html_email_message

    def _send_report_to_economists(self, email_message: str, destination_emails: List[str]) -> Any:
        email_params: Dict[str, Any] = {
            'Source': self.source_email,
            'Destination': {
                'ToAddresses': destination_emails,
            },
            'Message': {
                'Subject': {
                    'Data': 'Boletim de Inflação - Departamento de Economia da PUCPR',
                },
                'Body': {
                    'Html': {
                        'Data': email_message,
                    },
                },
            },
        }
        ses().send_email(**email_params)

    def _notify_sns(self) -> Any:
        report_sns_topic_arn: str = "arn:aws:sns:us-east-1:243883763338:datasciencepucpr-boletim-inflacao-send-email"
        notification_message: str = json.dumps("O boletim de inflação foi calculado e enviado com sucesso")
        sns().publish(report_sns_topic_arn, notification_message)

    def handle(self, economists_emails: List[str]) -> int:
        try:
            inflation_report: pd.DataFrame = self._get_inflation_report()
            inflation_summary: Dict[str, Any] = self._get_inflation_summary(inflation_report)
            html_email_message: str = self._generate_html_email_message(inflation_summary)
            self._send_report_to_economists(html_email_message, economists_emails)
            self._notify_sns()
            status_code: int = 200
        except Error as error:
            status_code: int = 400

        return status_code
