import yfinance as yf
import pandas as pd
from environment.trading_environment import TradingEnvironment
from models.dqn_agent import DQNAgent

# Download Stock Data
symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2025-02-14"
data = yf.download(symbol, start=start_date, end=end_date)

# Feature Engineering
data['SMA_5'] = data['Close'].rolling(window=5).mean()
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['Returns'] = data['Close'].pct_change()
data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)

# Testing Setup
env = TradingEnvironment(data)
agent = DQNAgent(state_size=4, action_size=3)

# Test (without exploration)
state = env.reset()
done = False

while not done:
    action = agent.act(state)
    next_state, reward, done, _ = env.step(action)
    state = next_state if next_state is not None else state

final_balance = env.balance
profit = final_balance - env.initial_balance

print(f"Final Balance after testing: ${final_balance:.2f}")
print(f"Total Profit: ${profit:.2f}")
