# N Back
# May 25, 2019
# TK

# This program runs the n_back test used to improve working memory. The
# inspiration for this project came from a Korean t.v. show Problematic Man,
# whose video can be seen (untranslated) here:
# https://www.youtube.com/watch?v=Ro5AI6nhzlQ

# First we start with 2_back

from random import randint
from graphics import *

def main(n = 2, size = 10):

  # Lists used to check answers
  problem = []
  nback = []
  answer = []

  # Graphic interface window
  win = GraphWin("N Back", 500, 500)

  # Text appearing in GUI
  txt = Text(Point(250, 250), '')
  txt.setSize(36)
  txt.draw(win)

  # Create numbers for nback problem
  for i in range(size):
    num = randint(0, 9)
    problem.append(num)

    # Change text on GUI
    txt.setText(num)

    # Can't check nback unless at least n numbers are known
    if i >= n:
      nback.append(num)

      # If nback match, O else X (rather than default boolean for reading ease)
      if problem[i - n] == nback[i - n]:
        answer.append('O')
      else:
        answer.append('X')

    # Give time to remember and forget
    time.sleep(2)
    txt.setText('')
    time.sleep(2)

  win.getMouse()
  win.close()

main()

