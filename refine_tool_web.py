import streamlit as st
import pandas as pd

# --------------------
# 精煉成本資料表
# --------------------
refine_data = [
    {"階段": "+0~+1", "起始": 0, "神金數": 1, "裝備件數": 0, "安精費": 10000},
    {"階段": "+1~+2", "起始": 1, "神金數": 1, "裝備件數": 0, "安精費": 20000},
    {"階段": "+2~+3", "起始": 2, "神金數": 1, "裝備件數": 0, "安精費": 30000},
    {"階段": "+3~+4", "起始": 3, "神金數": 1, "裝備件數": 0, "安精費": 40000},
    {"階段": "+4~+5", "起始": 4, "神金數": 5, "裝備件數": 1, "安精費": 100000},
    {"階段": "+5~+6", "起始": 5, "神金數": 10, "裝備件數": 2, "安精費": 220000},
    {"階段": "+6~+7", "起始": 6, "神金數": 15, "裝備件數": 3, "安精費": 470000},
    {"階段": "+7~+8", "起始": 7, "神金數": 25, "裝備件數": 4, "安精費": 910000},
    {"階段": "+8~+9", "起始": 8, "神金數": 50, "裝備件數": 6, "安精費": 1630000},
    {"階段": "+9~+10", "起始": 9, "神金數": 85, "裝備件數": 10, "安精費": 2740000},
    {"階段": "+10~+11", "起始": 10, "神金數": 135, "裝備件數": 22, "安精費": 5250000},
    {"階段": "+11~+12", "起始": 11, "神金數": 225, "裝備件數": 30, "安精費": 9000000},
    {"階段": "+12~+13", "起始": 12, "神金數": 375, "裝備件數": 45, "安精費": 14500000},
    {"階段": "+13~+14", "起始": 13, "神金數": 600, "裝備件數": 69, "安精費": 24500000},
    {"階段": "+14~+15", "起始": 14, "神金數": 900, "裝備件數": 98, "安精費": 42000000},
]

df = pd.DataFrame(refine_data)

# --------------------
# Streamlit 介面
# --------------------
st.set_page_config(page_title="精煉成本小工具", page_icon="⚒️")
st.title("⚒️ 精煉成本試算工具")

price_material = st.number_input("請輸入神金價格", value=69810)
price_equip = st.number_input("請輸入裝備價格", value=100000)
start_level = st.number_input("起始等級 (0~14)", min_value=0, max_value=14, value=6)
end_level = st.number_input("目標等級 (1~15)", min_value=1, max_value=15, value=15)

if st.button("▶ 計算成本"):
    selected = df[(df["起始"] >= start_level) & (df["起始"] < end_level)]

    total_metal = selected["神金數"].sum()
    total_equip = selected["裝備件數"].sum()
    total_safety_cost = selected["安精費"].sum()

    total_cost = total_metal * price_material + total_equip * price_equip + total_safety_cost

    st.subheader(f"✨ 精煉計算結果：從 +{start_level} → +{end_level}")
    st.write(f"👉 需要神金數量：{total_metal:,} 個")
    st.write(f"👉 需要裝備件數：{total_equip:,} 件")
    st.write(f"👉 安精費用合計：{total_safety_cost:,} Zeny")
    st.success(f"💰 總成本：{total_cost:,} Zeny")

    with st.expander("📋 查看每階段明細"):
        st.dataframe(selected.reset_index(drop=True))
