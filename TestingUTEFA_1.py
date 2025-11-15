import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("UTEFA_QuantiFi_Contestant_Dataset.csv")  

df['Day'] = pd.to_datetime(df['Day'])
df = df.set_index('Day')

print(df.head())


stocks = [f"Stock_{x}" for x in "ABCDE"]

df[stocks].plot(figsize=(10,5))
plt.title("Stock Prices Over Time (A–E)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(title="Stocks")
plt.show()

for stock in "ABCDE":
    price_col = f"Stock_{stock}"
    momentum_col = f"Stock_{stock}_Momentum_10d"
    
    sns.scatterplot(data=df, x=momentum_col, y=price_col)
    plt.title(f"Momentum vs Price ({stock})")
    plt.xlabel("10-Day Momentum")
    plt.ylabel("Price")
    plt.show()

for stock in "ABCDE":
    price_col = f"Stock_{stock}"
    volume_col = f"Stock_{stock}_Volume"

    fig, ax1 = plt.subplots(figsize=(10,5))

    # Plot price
    ax1.plot(df.index, df[price_col], color='blue', label='Price')
    ax1.set_ylabel("Price", color='blue')
    ax1.set_title(f"{stock}: Price and Volume Over Time")

    # Plot volume on second axis
    ax2 = ax1.twinx()
    ax2.bar(df.index, df[volume_col], color='gray', alpha=0.3, label='Volume')
    ax2.set_ylabel("Volume", color='gray')

    plt.show()


cols = [
    "Stock_A", "Stock_B", "Stock_C", "Stock_D", "Stock_E",
    "Stock_A_Momentum_10d", "Stock_B_Momentum_10d", "Stock_C_Momentum_10d",
    "Stock_D_Momentum_10d", "Stock_E_Momentum_10d",
    "Interest_Rate", "Economic_Growth", "Inflation"
]

corr = df[cols].corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Between Stocks, Momentum, and Economic Variables")
plt.show()