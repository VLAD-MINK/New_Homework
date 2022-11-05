
def ask_age():
  num1 = ''
  sign = ''
  num2 = ''
  while num1 == '' and sign == '' and num2 == '':
    try:
      num1 = int(input('Input your number 2: '))
      num2 = int(input('Input your number 1: '))
      sign = input('Input your sign: ')
      if sign == '+' or sign == '-' or sign == '*' or sign == '/':
        print(num1, sign, num2 )
      else:
        sign = ''
        raise ValueError
    except ValueError: 
      print('You need to write normal evaluation')
    if sign == '+':
      print(num1,sign,num2,'=',num1+num2)
    elif sign == '/':
      try:
        print(num1,sign,num2,'=',num1/num2)
      except:
        print('This is division by zero!!!')
    elif sign == '-':
      print(num1,sign,num2,'=',num1-num2)
    elif sign == '*':
      print(num1,sign,num2,'=',num1*num2)
  
ask_age()