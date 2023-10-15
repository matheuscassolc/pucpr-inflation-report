from typing import Any

from abc import abstract_method


class AmazonWebServices:
    _region: str = "us-east-1"

    @abstract_method
    @property
    def resource_name(self) -> str:
        raise NotImplementedError

    @property
    def client(self) -> Any:
        return boto3.client(self.resource_name, region=self._region)
