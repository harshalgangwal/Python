def ComputeBondPrice(T, C, y, F):
  Bond_Price: int = 0
  for i in range(T):
    Bond_Price += C / ((1 + y) ** i)
  Bond_Price += F / ((1 + y) ** T)
  return Bond_Price

def YTM(P, T, C, F, lower_bound=0.01, upper_bound=0.20, tol=0.00001):
    y = (lower_bound + upper_bound) / 2
    while True:
      Bond_Price = semianuual(T, C, y, F)
      diff = Bond_Price - P
      if abs(diff) < tol:
        break
      if diff > 0:
        upper_bound = y
      else:
        lower_bound = y
      y = (lower_bound + upper_bound) / 2
    return y

# Example usage
face_value = 1000
annual_coupon_rate = 0.05
years_to_maturity = 10
bond_market_price = 1085
annual_coupon_payment = face_value * annual_coupon_rate

ytm_value = YTM(bond_market_price, years_to_maturity, annual_coupon_payment, face_value)

print(f"Calculated YTM: {ytm_value * 100:.2f}%")
