import streamlit as st
import pandas as pd
import numpy as np
from src.models import Helicopter
from src.DataProcessing import ProcessData
from src.visualizer import Visualizer

st.set_page_config(page_title="Helicopter Drag Analyzer", layout="wide")

st.title("🚁 Helicopter Performance Analyzer")

st.sidebar.header("Cấu hình thông số")
st.sidebar.write("Điều chỉnh dải vận tốc để tính toán:")

# --- SECTION 1: SIDEBAR - VELOCITY RANGE INPUT ---
st.sidebar.header("Parameter Configuration")
st.sidebar.write("Adjust velocity range for calculation:")

# Example of the widgets with English labels:
v_min, v_max = st.sidebar.slider(
    "Velocity Range (m/s):",
    min_value=1, 
    max_value=200, 
    value=(10, 80),
    step=1
)

points = st.sidebar.select_slider(
    "Graph Resolution (Steps):",
    options=[50, 100, 200, 500],
    value=100
)

# Tạo v_range dựa trên input của user
v_range = np.linspace(v_min, v_max, points)

st.write("Upload your fleet CSV data to analyze optimal velocity and drag.")

# 1. Widget Upload File
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Khởi tạo range vận tốc
    v_range = np.linspace(10, 80, 100)
    
    # Sử dụng lại Class của bạn (với một chút chỉnh sửa để nhận file upload)
    processor = ProcessData(uploaded_file) 
    df = pd.read_csv(uploaded_file) # Đọc trực tiếp từ buffer
    
    clean_data = processor.ValidateData(df)
    model_lists = [Helicopter(item) for item in clean_data]

    if model_lists:
        # 2. Hiển thị bảng báo cáo ngay trên Web
        st.subheader("📊 Optimal Velocity Report")
        report_data = [obj.GetResult(v_range) for obj in model_lists]
        st.dataframe(pd.DataFrame(report_data), use_container_width=True)

        # 3. Hiển thị đồ thị
        st.subheader("📈 Drag Analysis Curves")
        # Chỉnh sửa hàm plotData để nó return về fig thay vì plt.show()
        plotter = Visualizer()
        fig = plotter.plotData(model_lists, v_range) 
        st.pyplot(fig)
    else:
        st.error("No valid data found in CSV!")