import os
import pandas as pd
import matplotlib.pyplot as plt

def read_csv_files(folder_path):
    data = {}
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    for subfolder in subfolders:
        csv_file_path = os.path.join(subfolder, 'safe_counts.csv')
        if os.path.exists(csv_file_path):
            df = pd.read_csv(csv_file_path)
            folder_name = os.path.basename(subfolder)
            data[folder_name] = df

    return data

def plot_data(data):
    plt.figure(figsize=(10, 6))
    
    for label, df in data.items():
        plt.plot(df['Interval'], df['Safe Count'], label=label)

    plt.xlabel('Interval')
    plt.ylabel('Safe Count')
    plt.title('Safe Count per Interval for Different Subfolders')
    plt.legend()
    plt.grid(True)

    plt.savefig('safe_counts_plot.png')
    plt.show()

def plot_cumulative_data(data):
    plt.figure(figsize=(10, 6))
    
    for label, df in data.items():
        cumulative_count = df['Safe Count'].cumsum()
        plt.plot(df['Interval'], cumulative_count, label=label)

    plt.xlabel('Interval')
    plt.ylabel('Cumulative Safe Count')
    plt.title('Cumulative Safe Count per Interval for Different Subfolders')
    plt.legend()
    plt.grid(True)
    plt.savefig('cumulative_safe_counts_plot.png')
    plt.show()

if __name__ == "__main__":
    folder_path = '/home/Fuzz4All/outputs/full_run/'  # 修改为包含子文件夹的主文件夹路径
    data = read_csv_files(folder_path)
    plot_data(data)
    plot_cumulative_data(data)
