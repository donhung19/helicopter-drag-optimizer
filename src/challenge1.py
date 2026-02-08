import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "model1": {
        "name": "helicopter1",
        "rho": 1.225, 
        "f_factor": 0.3,
        "weight": 800 * 9.81,
        "k_factor": 1.1,
        "rotor_radius": 3
    },
    "model2": {
        "name": "helicopter2",
        "rho": 1.225, 
        "f_factor": 0.5,
        "weight": 2000*9.81,
        "k_factor": 1.2,
        "rotor_radius": 6
    }
}

v_range = np.linspace(10,80,100)

class Helicopter:
    def __init__(self, data):
        self.name = data.get('name')
        self.rho = data.get('rho')
        self.f_factor = data.get('f_factor')

        self.weight = data.get('weight')
        self.k_factor = data.get('k_factor')
        self.rotor_radius = data.get('rotor_radius')

    def CalculateDrag(self, v_range):
        Dp = 0.5 * self.rho * v_range**2 * self.f_factor
        Di = (self.k_factor * self.weight**2) / (2 * self.rho * v_range**2 * (np.pi) * self.rotor_radius**2)
        return Dp, Di
    
    def FindOptimalVelocity(self, v_range, Dt):
        index_opt = np.argmin(Dt)
        v_opt = v_range[index_opt]
        D_min = Dt[index_opt]

        return v_opt, D_min
    
class ProcessData:
    def __init__(self, path_data):
        self.path = path_data

    def loadData(self):
        df = pd.read_csv(self.path)
        if df is None:
            return None
        return df
        
    def ValidateData(self, df):
        # convert to number, str
        cols_Tonumber = ['rho','f_factor','weight','k_factor','rotor_radius']
        for col in cols_Tonumber:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df['name'] = df['name'].astype(str)

        # delete rows have empty value
        df = df.dropna()

        # mask
        df = df[(df['f_factor'] > 0) & (df['rotor_radius'] > 0)]

        data_list = df.to_dict(orient='records')
    
        return data_list

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

        cols = len(model_lists)
        if cols == 0:
            return None
        fig, axs = plt.subplots(1, cols, figsize=(5 * cols, 5), sharey=True, squeeze=False)

        for index, obj in enumerate(model_lists):
            Dp, Di = obj.CalculateDrag(v_range)
            Dt = Dp + Di
            v_opt, d_min = obj.FindOptimalVelocity(v_range, Dt)

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



def main():
    # model_lists = []
    # for key in data:
    #     model = data[key]
    #     obj = Helicopter(model)
    #     model_lists.append(obj)

    path = "../data/fleet_data.csv"
    data = ProcessData(path)
    df = data.loadData()
    data_list = data.ValidateData(df)

    model_lists = [Helicopter(model) for model in data_list]

    plot = Visualizer()
    plot.plotData(model_lists, v_range)

   

if __name__ == "__main__":
    main()


            





        
