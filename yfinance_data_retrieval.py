import yfinance as yf
import pandas as pd

ticks = ["XLE", # ~25 largest US energy stocks (most liquid)
         "FENY", # Broad US energy (large, mid, small cap)
         "VDE", # Very similar to FENY
         "IYE", # US energy, large and mid cap
         "RYE", # Equal weight S&P500 energy stocks (mid cap heavy, higher volatility)
         "IXC", # Global energy exposure
         "XOP", # Equal weight E&P stocks, pure oil price exposure (small, mid cap heavy, high volatility)
         "PXE", # Similar to XOP, but factor-based weighting (momentum & value)
         "OIH", # US oil services, high cap
         "XES", # Similar to OIH (small, mid cap heavy)
] 

start = "2017-01-01"
end = "2023-01-01"
interval = "1wk" # or "1d"

for tick in ticks:
    df = yf.download(
        tick,
        start=start, # Inclusive
        end=end, # Exclusive
        interval=interval
    )
    df.columns = df.columns.droplevel(1)
    df = df.reset_index()
    df.to_csv(f"data/energy/{tick}_{start}_{end}_{interval}.csv", index=False)


