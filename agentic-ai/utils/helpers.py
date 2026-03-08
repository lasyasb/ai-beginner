import numpy as np

# Define possible actions
ACTIONS = {
    0: "HOLD",
    1: "BUY",
    2: "SELL"
}

def get_state(data, index):
    return np.array([
        float(data.loc[index, 'Close']),
        float(data.loc[index, 'SMA_5']),
        float(data.loc[index, 'SMA_20']),
        float(data.loc[index, 'Returns'])
    ])
