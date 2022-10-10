import datetime
import glob

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


# 設定
st.set_page_config(layout="wide")


# データ取得
targets = ['AAPL', 'TSLA', 'VOO']
files = glob.glob('data/trading_data_*')

data_list = [pd.read_csv(file, index_col=0) for file in files]
for id, df in enumerate(data_list):
    df.index = pd.to_datetime(df.index)
    data_list[id] = df


# サイドバー
st.sidebar.markdown("# 銘柄")
select_category = st.sidebar.selectbox('銘柄を選んでください。', targets)

st.sidebar.markdown("# 表示区間")
start_date = st.sidebar.date_input(
             '始まり',
             datetime.datetime(2022, 1, 1)
)

end_date = st.sidebar.date_input(
           '終わり',
           datetime.datetime.today()
)

st.sidebar.markdown("# 移動平均")
ma_days = st.sidebar.slider('スライドさせると移動平均を計算し直します。',
                    min_value=0,
                    max_value=int((end_date - start_date).days/2),
                    value=25,
                    step=1
)




# 可視化準備
idx = targets.index(select_category)
selected_data = data_list[idx]

ma_fig = selected_data['close'].rolling(window=ma_days).mean() # 移動平均

fig = go.Figure(data=[go.Candlestick(
                          x=selected_data[start_date: end_date].index,
                          open=selected_data['open'],
                          high=selected_data['high'],
                          low=selected_data['low'],
                          close=selected_data['close']
                      ),
                      go.Scatter(
                          x=selected_data[start_date: end_date].index,
                          y=ma_fig,
                          line=dict(color='orange',width=1)
                      )
                ]
)


# メイン
st.title('Trading App')
st.write(f'期間 {start_date} 〜 {end_date} の統計量')

describe_table = selected_data[start_date: end_date].describe()
trading_days = describe_table.loc['count', 'open'].round().astype(int)
max_value = describe_table.loc['max', 'high']
min_value = describe_table.loc['min', 'low']
today_volume = selected_data.iloc[-1][-1].round().astype(int)

describe_table = pd.DataFrame([f'{trading_days}日',
                                 f'${max_value}',
                                 f'${min_value}',
                                 today_volume,
                              ],
                              index=['取引日数','最高値', '最安値', '最新のVOLUME'],
                              columns=['値']
)
describe_table = describe_table.transpose()
describe_table = describe_table.style.format({'取引日数': '{:0}',
                                              '最高値': '{:2}',
                                              '最安値': '{:2}',
                                              '最新のVOLUME': '{:0}'
                                             }
)

st.table(describe_table)

st.write(f'{ma_days} 日移動平均')

fig.update_layout(title=select_category,
                  yaxis_title='株価',
                  font=dict(color='grey'),
                  hovermode='closest',
                  plot_bgcolor='white',
                  width=900,
                  height=500
)
fig.update_xaxes(showline=True,
                 linewidth=1,
                 linecolor='lightgrey',
                 color='grey'
)
fig.update_yaxes(showline=True,
                 linewidth=1,
                 linecolor='lightgrey',
                 color='grey'
)

st.plotly_chart(fig)

