import folium
from streamlit_folium import folium_static
import streamlit as st
import pandas as pd


df = pd.read_excel("リスト.xlsx")
store = df[["緯度", "経度", "店名", "都道府県"]].values

def AreaMarker(df,m):
    for data in store:
        folium.Marker([data[0], data[1]], tooltip=data[2] + "," + data[3]).add_to(m)


st.title('蕎麦屋訪問記')

"""
#
"""

col1, col2 = st.beta_columns(2)

with col1:
    st.image('a.JPG')

with col2:
    st.image('b.JPG')

"""
#
"""

st.header('蕎麦屋マップ')
choice_erea = st.sidebar.selectbox('地域を選択してください',
                ('', '北海道・東北', '関東', '甲信越', '中部',
                 '関西', '中国・四国', '九州', '沖縄'))

if choice_erea == '北海道・東北':
    m = folium.Map(location=[41.55087814221183, 140.91344916521436], zoom_start=6)
elif choice_erea == '関東':
    m = folium.Map(location=[35.681401760480355, 139.7670926112381], zoom_start=8)
elif choice_erea == '甲信越':
    m = folium.Map(location=[36.684499123269276, 138.18857933728128], zoom_start=8)
elif choice_erea == '中部':
    m = folium.Map(location=[35.171064072763976, 136.88153689773353], zoom_start=10)
elif choice_erea == '関西':
    m = folium.Map(location=[34.70264414718938, 135.4959720553945], zoom_start=10)
elif choice_erea == '中国・四国':
    m = folium.Map(location=[34.489227258798465, 133.36303572416085], zoom_start=8)
elif choice_erea == '九州':
    m = folium.Map(location=[32.79039170525756, 130.6899261265173], zoom_start=8)
elif choice_erea == '沖縄':
    m = folium.Map(location=[26.43511034499814, 127.82941845523354], zoom_start=10)
else:
    m = folium.Map(location=[36.23084969740848, 137.96437665542933], zoom_start=4)

AreaMarker(df, m) 
folium_static(m)

st.text('店名、場所は訪れた時点の情報です。閉店、移転されている可能性があります。')

"""
#
"""

df_1 = df.drop(['緯度', '経度'], axis=1)
df_1 = df_1.reindex(columns=['エリア', '都道府県', '店名'])

list_1 = st.checkbox('訪問リスト表示')

if list_1 == True:
    st.table(df_1)
