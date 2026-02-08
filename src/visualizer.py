import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import os

class Visualizer:
    def plotData(self, model_lists, v_range):

        # Dp, Di = [i, obj for i in model_lists].CalculateDrag(v_range)
        # Dt = Dp + Di

        # plt.plot(v_range, drag, label=object.name)
        # plt.xlabel('velocity')
        # plt.ylabel('drag')
        # plt.title('Drag plot')

        # plot = Visualizer()
        # for obj in model_lists:
        #     plot.plotData( obj ,v_range)
        # plt.legend()
        # plt.show() 

        total_models = len(model_lists)
       # max_cols_per_row = 3
        max_cols = 3  # Số subplot tối đa trên 1 hàng
        n_cols = min(total_models, max_cols)
        n_rows = math.ceil(total_models / max_cols)
        if total_models == 0:
            return None
        fig, axs = plt.subplots(n_rows, n_cols, figsize=(9 * n_cols, 9 * n_rows), dpi=120, sharey=False, squeeze=False)

        for index, obj in enumerate(model_lists):
            row_idx = index // n_cols  # Chia lấy phần nguyên để tìm hàng
            col_idx = index % n_cols   # Chia lấy phần dư để tìm cột
            ax = axs[row_idx, col_idx] # Truy cập đúng ô trong ma trận

            Dp, Di = obj.CalculateDrag(v_range)
            Dt = Dp + Di
            v_opt, d_min = obj.FindOptimalVelocity(v_range)

            ax.plot(v_range, Dp, label='Parasite Drag')
            ax.plot(v_range, Di, label='Induced Drag')
            ax.plot(v_range, Dt, linewidth=2, label='Total Drag')

            ax.set_title(model_lists[index].name)
            ax.set_xlabel('Velocity')
            ax.set_ylabel('Drag')
            ax.legend()

            ax.scatter(v_opt, d_min, color='red', zorder=5)
            ax.annotate(f'V_opt: {v_opt:.1f} m/s\nDrag: {d_min:.1f} N',
                        xy=(v_opt, d_min), 
                        xytext=(v_opt + 5, d_min + 500), # Đẩy chữ ra xa một chút
                        arrowprops=dict(arrowstyle='->', color='red'))
            
            table_data = [
                ["Weight (N)", f"{obj.weight:,.0f}"],
                ["R Radius (m)", f"{obj.rotor_radius:.1f}"],
                ["f Factor", f"{obj.f_factor:.3f}"],
                ["k Factor", f"{obj.k_factor:.2f}"],
                ["Rho (kg/m3)", f"{obj.rho:.3f}"]
            ]
            the_table = ax.table(
                cellText=table_data,
                colLabels=["Param", "Value"],
                loc='upper center', 
                cellLoc='center',
                bbox=[0.6, 0.6, 0.35, 0.3] # Căn bảng nằm ở góc trên bên phải, chiếm 35% rộng, 30% cao
            )
            the_table.auto_set_font_size(False)
            the_table.set_fontsize(8)

        plt.tight_layout()
        #plt.show()
        return fig