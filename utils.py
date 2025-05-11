import pandas as pd
import kagglehub

def load_data():
    path = kagglehub.dataset_download("vishakhdapat/customer-segmentation-clustering")
    print("Path to dataset files:", path)

    data = pd.read_csv(path + "\\customer_segmentation.csv")
    return data