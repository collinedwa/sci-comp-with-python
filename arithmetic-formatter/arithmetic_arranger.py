def arithmetic_arranger(problems, ans=False):
  firstnumbers = []
  operators = []
  secondnumbers = []
  answers = []
  lines = []
  
  if len(problems) > 5:
    return ('Error: Too many problems.')
  for i in range(len(problems)):
    problem = problems[i].split(' ')
    for n in problem:
      if len(n) > 4:
        return ('Error: Numbers cannot be more than four digits.')
    try:
        int(problem[0])
        int(problem[2])
    except:
        return("Error: Numbers must only contain digits.")
    linevalue = len(max(problem, key=len))+2    
    firstnumbers.append(problem[0].rjust(linevalue))
    operators.append(problem[1])
    secondnumbers.append((problem[1] + ' ' + problem[2].rjust(linevalue-2)))
    lines.append("-"*linevalue)
    if problem[1] == "+":
      answers.append(str(int(problem[0])+int(problem[2])).rjust(linevalue))
    if problem[1] == "-":
      answers.append(str(int(problem[0])-int(problem[2])).rjust(linevalue))
    elif "+" not in problem[1] and "-" not in problem[1]:
      return ("Error: Operator must be '+' or '-'.")
    
# print(firstnumbers,operators,secondnumbers,lines,answers)   
  if ans == False:
    return('    '.join(firstnumbers) + '\n' + '    '.join(secondnumbers) + '\n' + '    '.join(lines)) 
  else:
    return('    '.join(firstnumbers) + '\n' + '    '.join(secondnumbers) + '\n' + '    '.join(lines) + '\n' + '    '.join(answers))