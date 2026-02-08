import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

v_range = np.linspace(10, 80, 100)

class Helicopter:
    def __init__(self, data):
        self.name = data.get('name')
        self.rho = data.get('rho')
        self.f_factor = data.get('f_factor')
        self.weight = data.get('weight')
        self.k_factor = data.get('k_factor')
        self.rotor_radius = data.get('rotor_radius')

    def CalculateDrag(self, v):
        # Parasite Drag
        Dp = 0.5 * self.rho * v**2 * self.f_factor
        # Induced Drag: Pi không bình phương trong công thức chuẩn Di = (k*W^2) / (2*rho*v^2*pi*R^2)
        Di = (self.k_factor * self.weight**2) / (2 * self.rho * v**2 * np.pi * self.rotor_radius**2)
        return Dp, Di
    
class ProcessData:
    def __init__(self, path_data):
        self.path = path_data

    def loadData(self):
        try:
            return pd.read_csv(self.path)
        except FileNotFoundError:
            print(f"Lỗi: Không tìm thấy file tại {self.path}")
            return None
        
    def ValidateData(self, df):
        if df is None: return []
        
        # SỬA LỖI 1: Gán lại vào từng cột
        cols_Tonumber = ['rho','f_factor','weight','k_factor','rotor_radius']
        for col in cols_Tonumber:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df['name'] = df['name'].astype(str)

        # Xóa dòng trống (xử lý Heli_Error_Missing)
        df = df.dropna()

        # Lọc giá trị dương (xử lý Heli_Error_Negative, Heli_Error_Zero_Radius)
        df = df.query("f_factor > 0 and rotor_radius > 0 and weight > 0")

        return df.to_dict(orient='records')

class Visualizer:
    def plotData(self, model_lists, v_range):
        cols = len(model_lists)
        if cols == 0:
            print("Không có dữ liệu hợp lệ để vẽ.")
            return

        # SỬA LỖI 2: squeeze=False giúp axs luôn là mảng kể cả khi cols=1
        fig, axs = plt.subplots(1, cols, figsize=(5 * cols, 5), sharey=True, squeeze=False)

        for index, obj in enumerate(model_lists):
            Dp, Di = obj.CalculateDrag(v_range)
            Dt = Dp + Di

            ax = axs[0, index] # Truy cập mảng 2 chiều
            ax.plot(v_range, Dp, '--', label='Parasite Drag')
            ax.plot(v_range, Di, '--', label='Induced Drag')
            ax.plot(v_range, Dt, linewidth=2, color='black', label='Total Drag')

            ax.set_title(obj.name)
            ax.set_xlabel('Velocity (m/s)')
            ax.set_ylabel('Drag (N)')
            ax.legend()

        plt.tight_layout()
        plt.show()    

def main():
    path = "../data/fleet_data.csv" # Đảm bảo file này tồn tại đúng tên
    data_proc = ProcessData(path)
    df = data_proc.loadData()
    
    if df is not None:
        data_list = data_proc.ValidateData(df)
        model_lists = [Helicopter(model) for model in data_list]

        plot = Visualizer()
        plot.plotData(model_lists, v_range)

if __name__ == "__main__":
    main()