def arithmetic_arranger(problems, torf=True):
  if torf:
    nums = ''
    dens = ''
    sums = ''
    # error when too many problems
    if len(problems) > 5:
      return 'Error: Too many problems.'
    # split problem into components
    for k in problems:
      l = (k.split(' '))
      num = l[0]
      op = l[1]
      den = l[2]
      # error when numbers are too long or non-numeric
      if len(num) > 4 or len(den) > 4:
        return 'Error: Numbers cannot be more than four digits.'
      if not num.isnumeric() or not den.isnumeric():
        return 'Error: Numbers must only contain digits.'
      # execute code if operators are correct
      if  op == '+' or op == '-':
        # set length of sum and top, bottom and line values
        length = max(len(num), len(den)) + 2
        top = str(num).rjust(length)
        bottom = op + str(den).rjust(length - 1)
        sum = ''
        for s in range(length):
          sum += '-'
        # add to the overall string
        nums += top + '    '
        dens += bottom + '    '
        sums += sum + '    '
      else:
        return "Error: Operator must be '+' or '-'."
    # strip out spaces to the right of the string
    nums= nums.rstrip()
    dens= dens.rstrip()
    sums= sums.rstrip()

    arranged_problems = nums + '\n' + dens + '\n' + sums
    return arranged_problems

problems =["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

print(arithmetic_arranger(problems))