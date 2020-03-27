# Time complexity 0(N) and Space complexity O(1)


def buy_sell_stock_max_profit(arr):

    if arr is None:
        return 0

    min_profit = float("inf")
    max_profit = 0

    for price in arr:
        min_profit = min(min_profit, price)
        profit = price - min_profit
        max_profit = max(profit, max_profit)
    return max_profit


print(buy_sell_stock_max_profit([250, 200, 150, 300, 400, 500, 800, 500, 280]))
