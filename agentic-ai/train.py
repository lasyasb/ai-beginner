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

# Training Setup
env = TradingEnvironment(data)
agent = DQNAgent(state_size=4, action_size=3)
batch_size = 32
episodes = 500

# Training Loop
for episode in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward

    agent.replay(batch_size)
    print(f"Episode {episode+1}/{episodes}, Total Reward: {total_reward:.2f}")

print("Training Complete!")
