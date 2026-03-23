import streamlit as st
import numpy as np 
import pandas as pd

#画像
from PIL import Image


st.title("streamlit/超入門")

st.write("DataFrame")
st.badge("表", color="green")
    

df=pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})

#表の表示　
st.dataframe(df.style.highlight_max(axis=0), width=500, height=100)
#st.write(df) 
# st.writeは引数で選択できない
st.table(df)
#tableは静的、dataframeは動的

#マジックコマンド
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np 
import pandas as pd
```

"""

df=pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
st.badge("グラフ", color="blue")

st.dataframe(df)
#折れ線グラフ
st.line_chart(df)
#エリアチャート
st.area_chart(df)
#棒グラフ
st.bar_chart(df)

st.badge("地図", color="orange")

df=pd.DataFrame(
    np.random.rand(50,2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"]#緯度経度
)

st.map(df)

st.write("Display Image")
#画像読み込み
img=Image.open(r"C:\Users\81701\Pictures\Camera Roll\AUS\S__39600159_0.jpg")
st.image(img,caption="landscape",use_column_width=True)
#use_column_widthは画像の幅を画面いっぱいにするオプション

st.latex(r'''
         a^2+b^2=c^2
''' )
