#!/usr/bin/python
"""
A simple script to analyze the chance of getting
4 of the same card (Hearts/Clubs/Spades/Diamonds) at
least once from 13 random cards.
From discussion around Da Lao Er.
"""

import argparse
import random


def deal_hands():
  """Function to deal 4 hands of 13 cards randomly."""
  cards = list(range(52))
  hands = [[] for x in range(4)]
  random.shuffle(cards)
  for i in range(4):
    hands[i] = cards[i*13:(i+1)*13]
  return hands

def examine_hand(hand):
  """Analyze given hand and return number of times with 4 of the same cards."""
  nums = [x % 13 for x in hand]
  four = 0
  for i in range(13):
    count = nums.count(i)
    if count == 4:
      four += 1
  return four

def main():
  """Main function to update network stats."""
  parser = argparse.ArgumentParser(
      description='Randomly deal rounds of cards')
  parser.add_argument('-c', '--count', default=1000, type=int, nargs='?',
                      help='count of number of hands dealt')
  parser.add_argument('-v', '--verbose',
                      action='store_true')  # on/off flagparser.
  args = parser.parse_args()

  success = 0
  for i in range(args.count):
    hands = deal_hands()
    for hand in hands:
      fourcards = examine_hand(hand)
      if fourcards > 0:
        if args.verbose:
          print("%d: %d" % (i, fourcards))
        success += 1
  print(success / args.count)

if __name__ == '__main__':
  main()
