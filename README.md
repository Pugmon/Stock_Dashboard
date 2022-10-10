# 株価データのダッシュボード

<img width="1429" alt="stock_app_screen" src="https://user-images.githubusercontent.com/67322317/194794859-76748823-6812-451c-9461-ae107b17e6e3.png">

![stock_app_image](https://user-images.githubusercontent.com/67322317/194796205-3d714d04-7868-45a5-9a1d-57d85ad0ce66.gif)

## アプリの概要
株価データを表示するダッシュボード
### サイドバー
- 銘柄をリスト内から選択
- 日付をカレンダー機能で変更
- 移動平均の日数をスライドバーで変更
### メイン
- 統計量は指定した期間内について計算
- 選択した銘柄及び移動平均をグラフ表示

## 使い方
```
git clone  
streamlit run stock_dashboard.py
```

## データ
- IEXのAPIでアプリに使用するデータを取得してCSVファイルとしてdataフォルダに保存
- ```get_trading_data.py``` でIEXからデータ取得 (APIのTOKENが必要)

## 環境
- macOS
- Visual Studio Code
- python==3.10.6
- pandas==1.5.0
- pandas-datareader==0.10.0
- plotly==5.10.0
- streamlit==1.13.0　　

## 今後の改善点
- リアルタイムでのデータ取得
- デバイスに応じたサイズ変更
- デザインの改善
