from typing import Any

from aws import AmazonWebServices


class SimpleNotificationService(AmazonWebServices):
    @property
    def resource_name(self) -> str:
        return "sns"

    def publish(self, topic_arn: str, message: str) -> Any:
        self.client.publish(
            TopicArn=topic_arn,
            Message=message
        )
