import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import utils.pantry as pantry
import utils.pantry as pantry

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Smart Pantry Tracker",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

[data-testid="metric-container"]{
    background-color:#1e1e1e;
    border-radius:12px;
    padding:15px;
    border:1px solid #333;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# LOAD DATA
# -----------------------------------

pantry.load_data()

# -----------------------------------
# TITLE
# -----------------------------------

st.title("Smart Pantry & Food Waste Tracker")

st.caption(
    "Track groceries, expiry dates, pantry value, and reduce food waste."
)

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("Add New Item")

categories = [
    "Dairy",
    "Vegetables",
    "Fruits",
    "Grains",
    "Bakery",
    "Frozen",
    "Snacks",
    "Beverages",
    "Spices",
    "Meat"
]

units = [
    "kg",
    "grams",
    "liters",
    "ml",
    "pcs",
    "packs",
    "bottles"
]

item = st.sidebar.text_input("Item Name")

category = st.sidebar.selectbox(
    "Category",
    categories
)

unit = st.sidebar.selectbox(
    "Unit",
    units
)

price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    step=1.0
)

qty = st.sidebar.number_input(
    "Quantity",
    min_value=1,
    step=1
)

fresh_for = st.sidebar.number_input(
    "Fresh For (Days)",
    min_value=1,
    step=1
)

# -----------------------------------
# ADD ITEM
# -----------------------------------

if st.sidebar.button("Add Item"):

    if item.strip() != "":

        pantry.add_item(
            item,
            category,
            unit,
            price,
            qty,
            fresh_for
        )

        st.sidebar.success(
            f"{item} added successfully"
        )

        st.rerun()

# -----------------------------------
# EMPTY CHECK
# -----------------------------------

if not pantry.grocery_list:

    st.warning("Your pantry is empty")
    st.stop()

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

data = []

expired_count = 0
expiring_soon_count = 0
low_stock_count = 0

total_value = 0

health_score = 100

for a in pantry.grocery_list:

    date_added = datetime.strptime(
        a["date_added"],
        "%d-%m-%Y"
    )

    days_passed = (
        datetime.now() - date_added
    ).days

    days_left = a["fresh_for"] - days_passed

    total_item_value = (
        a["price"] * a["qty"]
    )

    total_value += total_item_value

    # -----------------------------------
    # STATUS
    # -----------------------------------

    if days_left <= 0:

        status = "Expired"

        expired_count += 1

        health_score -= 10

    elif days_left <= 2:

        status = "Expiring Soon"

        expiring_soon_count += 1

        health_score -= 5

    else:

        status = "Fresh"

    # -----------------------------------
    # LOW STOCK
    # -----------------------------------

    if a["qty"] <= 2:

        low_stock = "Low"

        low_stock_count += 1

    else:

        low_stock = "Normal"

    data.append({

        "Item": a["item"].title(),

        "Category": a["category"],

        "Quantity": f'{a["qty"]} {a["unit"]}',

        "Qty Number": a["qty"],

        "Price": a["price"],

        "Total Value": total_item_value,

        "Days Left": days_left,

        "Stock": low_stock,

        "Status": status
    })

df = pd.DataFrame(data)

# -----------------------------------
# SORTING
# -----------------------------------

status_order = {
    "Expired": 0,
    "Expiring Soon": 1,
    "Fresh": 2
}

df["sort_order"] = df["Status"].map(
    status_order
)

df = df.sort_values(
    by=["sort_order", "Days Left"]
)

df = df.drop(columns=["sort_order"])

# -----------------------------------
# METRICS
# -----------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Items",
    len(df)
)

col2.metric(
    "Pantry Value",
    f"${total_value:.2f}"
)

col3.metric(
    "Expired",
    expired_count
)

col4.metric(
    "Expiring Soon",
    expiring_soon_count
)

col5.metric(
    "Low Stock",
    low_stock_count
)

# -----------------------------------
# HEALTH SCORE
# -----------------------------------

st.subheader("Pantry Health Score")

if health_score >= 80:

    st.success(f"{health_score}/100")

elif health_score >= 50:

    st.warning(f"{health_score}/100")

else:

    st.error(f"{health_score}/100")


# -----------------------------------
# SEARCH + FILTER
# -----------------------------------

st.subheader("Search Pantry")

search = st.text_input(
    "Search Item"
)

selected_category = st.selectbox(
    "Filter By Category",
    ["All"] + list(df["Category"].unique())
)

filtered_df = df.copy()

if search:

    filtered_df = filtered_df[
        filtered_df["Item"]
        .str.lower()
        .str.contains(search.lower())
    ]

if selected_category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

# -----------------------------------
# TABS
# -----------------------------------

tab1, tab2 = st.tabs([
    "Inventory",
    "Analytics"
])



# ===================================
# TAB 1
# ===================================

with tab1:

    st.subheader("Pantry Inventory")

    def color_status(val):

        if val == "Expired":
            return "background-color: #ff4b4b; color: white"

        elif val == "Expiring Soon":
            return "background-color: #ffa500; color: black"

        elif val == "Fresh":
            return "background-color: #4CAF50; color: white"

        return ""
    filtered_df = filtered_df.drop(
    columns=["Qty Number"]
)
    styled_df = filtered_df.style.map(
        color_status,
        subset=["Status"]
)

    st.dataframe(
        styled_df,
        use_container_width=True
    )

    # -----------------------------------
    # DELETE ITEM
    # -----------------------------------

    st.subheader("Delete Item")

    item_names = [
        a["item"]
        for a in pantry.grocery_list
    ]

    delete_item = st.selectbox(
        "Select Item",
        item_names
    )

    if st.button("Delete Selected Item"):

        pantry.delete_item(delete_item)

        st.success(
            f"{delete_item} deleted"
        )

        st.rerun()

    # -----------------------------------
    # EXPIRING ITEMS
    # -----------------------------------

    st.subheader("Items Expiring Soon")

    expiring_df = df[
        df["Status"] != "Fresh"
    ]

    if not expiring_df.empty:

        st.dataframe(
            expiring_df,
            use_container_width=True
        )

    else:

        st.success(
            "No items are expiring soon"
        )

# ===================================
# TAB 2
# ===================================

with tab2:

    st.subheader("Analytics Dashboard")

    chart1, chart2 = st.columns(2)

    # -----------------------------------
    # CATEGORY DONUT CHART
    # -----------------------------------

    with chart1:

        category_chart = (
            df.groupby("Category")
            .size()
        )

        fig_category = px.pie(
            values=category_chart.values,
            names=category_chart.index,
            hole=0.5,
            title="Category Distribution"
        )

        st.plotly_chart(
            fig_category,
            use_container_width=True
        )

    # -----------------------------------
    # STATUS FUNNEL
    # -----------------------------------

    with chart2:

        status_chart = (
            df.groupby("Status")
            .size()
        )

        fig_status = px.funnel_area(
            names=status_chart.index,
            values=status_chart.values,
            title="Freshness Status"
        )

        st.plotly_chart(
            fig_status,
            use_container_width=True
        )

    # -----------------------------------
    # TREEMAP
    # -----------------------------------

    money_df = (
        df.groupby("Category")["Total Value"]
        .sum()
        .reset_index()
    )

    fig_money = px.treemap(
        money_df,
        path=["Category"],
        values="Total Value",
        title="Pantry Value Distribution"
    )

    st.plotly_chart(
        fig_money,
        use_container_width=True
    )

    # -----------------------------------
    # EXPIRY SCATTER
    # -----------------------------------

    fig_timeline = px.scatter(
        df,
        x="Item",
        y="Days Left",
        color="Status",
        size="Total Value",
        hover_data=["Category"],
        title="Expiry Risk Overview"
    )

    st.plotly_chart(
        fig_timeline,
        use_container_width=True
    )

# -----------------------------------
# EXPORT CSV
# -----------------------------------

st.divider()

st.subheader("Export Pantry Data")

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="pantry_report.csv",
    mime="text/csv"
)
