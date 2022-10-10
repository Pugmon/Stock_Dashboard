import datetime

import pandas as pd
import pandas_datareader.data as web


# IEXから株価データの読み込む関数
def get_data(targets: list, start: datetime, end: datetime, token: str):
    trading_data = []
    for target in targets:
        target_data = web.DataReader(
            target, 'av-daily', start, end, api_key=token
        )
        trading_data.append(target_data)
        target_data.to_csv(
            f'trading_data_{target}_{datetime.datetime.utcnow()}.csv'
        )


if __name__ == "__main__":
    targets = ['AAPL', 'TSLA', 'VOO'] # 銘柄
    start = datetime.datetime(2015, 1, 1) # 取得開始日
    end = datetime.date.today() # 取得最終日
    API_TOKEN = 'API_TOKEN'
    get_data(targets, start, end, API_TOKEN)