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
        fig, axs = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows), dpi=120, sharey=True, squeeze=False)

        for index, obj in enumerate(model_lists):
            Dp, Di = obj.CalculateDrag(v_range)
            Dt = Dp + Di
            v_opt, d_min = obj.FindOptimalVelocity(v_range)

            axs[0,index].plot(v_range, Dp, label='Parasite Drag')
            axs[0,index].plot(v_range, Di, label='Induced Drag')
            axs[0,index].plot(v_range, Dt, linewidth=2, label='Total Drag')

            axs[0,index].set_title(model_lists[index].name)
            axs[0,index].set_xlabel('Velocity')
            axs[0,index].set_ylabel('Drag')
            axs[0,index].legend()

            axs[0,index].scatter(v_opt, d_min, color='red', zorder=5)
            axs[0,index].annotate(f'V_opt: {v_opt:.1f} m/s\nDrag: {d_min:.1f} N',
                        xy=(v_opt, d_min), 
                        xytext=(v_opt + 5, d_min + 500), # Đẩy chữ ra xa một chút
                        arrowprops=dict(arrowstyle='->', color='red'))

        plt.tight_layout()
        plt.show()