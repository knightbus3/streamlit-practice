import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

import webbrowser, os


# #Appleのみの株価取得
# aapl=yf.Ticker("AAPL")
# hist=aapl.history()

# hist.index=hist.index.strftime("%d-%B-%Y")
# #print(hist.head())

# #Closeのみを取り出す
# hist=hist[["Close"]]
# hist.columns=["Apple"]
# #print(hist.head())

# #行と列を入れ替える
# hist=hist.transpose()
# hist.index.name="Company"
# print(hist)



#複数社の株価取得
days=20
tickers={
    "Apple":"AAPL",
    "Google":"GOOGL",
    "Microsoft":"MSFT",
    # "Toyota":"7203.T",
    # "HONDA":"7267.T",
    # "Sony":"6758.T",
    # "Japan Airlines":"9201.T"
}

#空のデータフレームを用意
df=pd.DataFrame()
for company in tickers.keys():
     tkr=yf.Ticker(tickers[company])
     hist=tkr.history(period=f"{days}d")
     #hist.index=hist.index.strftime("%d-%B-%Y")
     hist=hist[["Close"]]
     hist.columns=[company]
     hist=hist.transpose()
     hist.index.name="Name"
     df=pd.concat([df,hist])


companies=["Apple", "Google"]

#カラム名、インデックス名で取得
data=df.loc[companies]

#行と列を入れ替える
data=data.transpose().reset_index()
data=data.rename(columns={"index":"Date"})
data=pd.melt(data, id_vars=["Date"]).rename(
        columns={
             "variable": "Name",
             "value": "Stock prices"}
     )

#ｙ軸の範囲を指定してグラフを作成
ymax, ymin=300, 250
chart=(
     alt.Chart(data).mark_line(opacity=0.8, clip=True)#Clipはグラフの外に線が出ないようにする
     .encode(
          x="Date:T",
          y=alt.Y("Stock prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
          color="Name:N"
     )
 )

chart.save("chart.html")
webbrowser.open("file://" + os.path.realpath("chart.html"))
