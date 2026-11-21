import numpy as np

def feature_scaling(X: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    m,n=X.shape
    feature_min=X.min(axis=0)
    feature_max=X.max(axis=0)
    mean=X.mean(axis=0)
    standardized_data=np.zeros((m,n))
    normalized_data=np.zeros((m,n))
    std=X.std(axis=0)
    for i in range(0,m):
        standardized_data[i]=(X[i]-mean)/std
        normalized_data[i]=(X[i]-feature_min)/(feature_max-feature_min)



    return standardized_data, normalized_data