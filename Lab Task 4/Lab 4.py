# Dynamic - N queens problem

def initialize(n):
  for key in ['queen','row','col','nwtose','swtone']:
    board[key] = {}
  for i in range(n):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][i] = 0
  for i in range(-(n-1),n):
    board['nwtose'][i] = 0
  for i in range(2*n-1):
    board['swtone'][i] = 0

'''  for row in sorted(board['queen'].keys()):
        print((row,board['queen'][row]))
''' 
def printboard():
  l = len(board['queen'].keys())
  for row in sorted(board['queen'].keys()):
    print("")
    for j in range(l):
        print("----",end="")
    print("\n|",end ="")
    for i in range(l):
        if i == board['queen'][row]:
            print(" Q |",end="")
        else:
            print("   |",end="")
  print("")
  for j in range(l):
        print("----",end="")

def free(i,j):
  return(board['row'][i] == 0 and board['col'][j] == 0 and board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)

def addqueen(i,j):
  board['queen'][i] = j
  board['row'][i] = 1
  board['col'][j] = 1
  board['nwtose'][j-i] = 1
  board['swtone'][j+i] = 1

def undoqueen(i,j):
  board['queen'][i] = -1
  board['row'][i] = 0
  board['col'][j] = 0
  board['nwtose'][j-i] = 0
  board['swtone'][j+i] = 0

def placequeen(i):
  n = len(board['queen'].keys())
  for j in range(n):
    if free(i,j):
      addqueen(i,j)
      print("\nadd queen:\ni:{} j:{} \n".format(i,j))
      printboard()
      if i == n-1:
        return(True)
      else:
        extendsoln = placequeen(i+1)
      if extendsoln:
        return(True)
      else:
        undoqueen(i,j)
        print("\nundo:\ni:{} j:{} \n".format(i,j))
        printboard()
  else:
    return(False)

board = {}
n = int(input("How many queens? "))
initialize(n)
#print("Final solution")
if placequeen(0):
  print("\n\nFinal solution")
  printboard()

