import datetime

import pandas as pd
import pandas_datareader.data as web


# IEXから株価データの読み込む関数
def get_data(targets: list, start: datetime, end: datetime, token: str) -> list:
    trading_data = []
    for target in targets:
        target_data = web.DataReader(
            target, 'av-daily', start, end, api_key=token
        )
        target_data.index = pd.to_datetime(target_data.index)
        trading_data.append(target_data)
    return trading_data


if __name__ == "__main__":
    targets = ['AAPL', 'TSLA', 'VOO']
    API_TOKEN = 'IEX_API_TOKEN'
    start = datetime(2015, 1, 1)
    end = datetime.date.today()
    get_data()