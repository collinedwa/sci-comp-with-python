import copy
import random
# Consider using the modules imported above.
class Hat:
  def __init__(self,**balls):
    self.contents = []
    for key, value in balls.items():
        self.contents.extend([key]*value)
  def draw(self,num_balls_drawn):
    if num_balls_drawn > int(len(self.contents)):
        return self.contents
    else:
        result = []
        for i in range(num_balls_drawn):
            pos = random.randrange(len(self.contents))
            result.append(self.contents[pos])
            self.contents.pop(pos)
        return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_result = []
  prob = 0
  for key, value in expected_balls.items():
        expected_result.extend([key]*value)
  contents_copy = copy.deepcopy(hat.contents)
  for i in range(num_experiments):
    newdraw = hat.draw(num_balls_drawn)
    hat.contents = copy.deepcopy(contents_copy)
    truecount = 0
#   print(newdraw, expected_result)
    for n in expected_result:
        for m in newdraw:
            if m == n:
                newdraw.pop(newdraw.index(m))
                truecount +=1
                break
    if truecount == len(expected_result):
        prob += 1
#       print('true')
#   else:
#       print('false')
  return prob/num_experiments