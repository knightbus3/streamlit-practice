import yfinance as yf
import pandas as pd
import altair as alt
import streamlit as st

st.title("US株価可視化ツール")

st.sidebar.write("""
# GAFA株価
表示日数を変更
""")

st.sidebar.write("""
## 表示日数を選択
""")

days=st.sidebar.slider("日数", min_value=1, max_value=50, value=20, step=1)

st.write(f"""
### 過去{days}日間の株価
""")

st.sidebar.write("""
## 株価の範囲指定
""")

ymin, ymax = st.sidebar.slider(
     "範囲の指定",
     0.0, 3500.0,  (0.0, 3500.0) 
)

tickers={
    "Apple":"AAPL",
    "Google":"GOOGL",
    "Microsoft":"MSFT"
}


df=pd.DataFrame()
for company in tickers.keys():
     tkr=yf.Ticker(tickers[company])
     hist=tkr.history(period=f"{days}d")
     hist.index=hist.index.strftime("%d-%B-%Y")
     hist=hist[["Close"]]
     hist.columns=[company]
     hist=hist.transpose()
     hist.index.name="Name"
     df=pd.concat([df,hist])

companies= st.multiselect("会社名の選択",
               list(df.index),
                default=["Apple", "Google"]

)

if not companies:
     st.error("最低一社は選ぶ")
else:
     #グラフを表示
     data=df.loc[companies]
     st.write("### 株価", data.sort_index())
     #表の表示
     data=data.transpose().reset_index()
     #data=data.rename(columns={"index":"Date"}),
     data=pd.melt(data, id_vars=["Date"]).rename(
        columns={
             "variable": "Name",
             "value": "Stock prices"}
     )
            
     chart=(
        alt.Chart(data).mark_line(opacity=0.8, clip=True)#Clipはグラフの外に線が出ないようにする            
        .encode(
                x="Date:T",
                y=alt.Y("Stock prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color="Name:N"
        )
     )
     st.altair_chart(chart, use_container_width=True)
     #chart.show()
    
                



