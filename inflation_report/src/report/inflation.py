from typing import Any

import pandas as pd


class InflationReporter:
    def __init__(self, reference_date: str) -> None:
        self.reference_date: str = reference_date

    def generate_report(self) -> pd.DataFrame:
        pass
