import json

from inflation_report.src.core import Handler


def lambda_handler(event, context):
    economists_emails: List[str] = [
        "matheuscassolc@hotmail.com"
    ]
    status_code: int = Handler().handle(economists_emails)
    succeeded: bool = status_code == 200
    status: str = "SUCESSO" if succeeded else "ERRO"
    body_message: str = f"Execução completa: {status}"
    return {
        'statusCode': status_code,
        'body': json.dumps(body_message, ensure_ascii=False).encode('utf-8')
    }
