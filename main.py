import random as rd
import pandas as pd

def shopDefine():
  no_goods = 100
  no_locations = 10
  goodLocation = [rd.randrange(0,no_locations) for i in range(no_goods)]
  goodQuantity = [rd.randrange(20,100) for i in range(no_goods)]
  tot = [0 for i in range(no_locations)]
  for i in range(no_goods):
    tot[goodLocation[i]] = tot[goodLocation[i]] + goodQuantity[i]
    
  buffer = 5
  Max = [tot[i] + buffer for i in range(no_locations)]
  shopStock = pd.DataFrame({
    "Item #":[i for i in range(no_goods)],
    "Location":goodLocation,
    "Quantity":goodQuantity,
    "Timestamp":[0 for i in range(no_goods)],
    "Reference":[2 for i in range(no_goods)],  # (0 for purchase, 1 for partial restock, 2 for full shop restock)
    "Timestamp":[0 for i in range(no_goods)]
  })
  return shopStock,Max

goodsLog, MaxSpace = shopDefine()
