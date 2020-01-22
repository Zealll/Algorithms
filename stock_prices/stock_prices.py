#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = prices[1] - prices[0]
  for i in range(1, len(prices)):
      j = 0
      while j < i:
          # print(profit)
          if prices[i] - prices[j] > profit:
              profit = prices[i] - prices[j]
          j += 1
  return profit
  # for i in range(1, len(prices)):
  #   if prices[i] - prices[i - 1] > highest:
  #     highest = prices[i] - lowest
  #     print(highest)
  #     print('lowest',lowest)
  #     if lowest > prices[i]:
  #       lowest = prices[i]
      # print(highest)
  # for i in range(len(prices)):
  #   # if i <= len(prices) - 2 and lowest < prices[i+1] and lowest > prices[i] and lowest > prices[i-1]:
  #   if i <= len(prices) - 2 and prices[i] < prices[i+1] and prices[i] < prices[i-1]:
  #     lowest = prices[i]
  #     index = i
  #     # print(prices[i])

  # for i in range(index, len(prices)):
  #   if i <= len(prices) - 2 and prices[i] < prices[i+1] and highest < prices[i + 1]:
  #     highest = prices[i + 1]
  #     print(highest)
  
  # print(highest, lowest)
  # return highest - lowest
  # return highest
print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))