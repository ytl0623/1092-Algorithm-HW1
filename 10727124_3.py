#  演算法分析機測
#  學號 10727124 10727125 10727155
#  姓名 劉宇廷    石慕評    曾博暉
#  中原大學資訊工程學系
from sympy import *

def ReadInput( list ) :
  while 1 :
    value = input( "Please enter Differential Equation : " )
    value = value.replace( " ", "" )     # remove space in string
    if ( value != "0" ) :
      #print( value )
      list.append(value)
    else :
      break

def CheckSqrt( ans ) :
  if ( ans.find("sqrt") != -1 ) :
    nSqrt = ans.count( "sqrt" )
    start = 0
    quote = 0
    num = 0
    while nSqrt > 0 :
      x = ans.find( "sqrt", start )
      start = x
      quote = ans.find( ")", x )
      num = int( ans[x+5:quote])
      ans = ans.replace( ans[x:quote+1], str(num) + "^(1/2)", 1 )
      nSqrt = nSqrt - 1
    return ans
  else :
    return ans

def CheckPower( ans ) :
  if ( ans.find( "**" ) != -1 ) :
    n = ans.count( "**" )
    beg = 0
    while ( n > 0 ) :
      y = ans.find( "**", beg )
      beg = y
      ans = ans.replace( ans[y:y+2], "^", 1 )
      n = n - 1
    return ans
  else :
    return ans

def SecondOrderDE( a, b, c ) :                                             
  x = symbols('x')
  y = Function('y')
  
  ode = a*diff(y(x),x,2) + b*diff(y(x),x) + c*y(x)
  ans = str(dsolve( ode, y(x) ))
  ans = ans.replace( "Eq(y(x), ", "" )
  ans = "y=" + ans
  ans = CheckSqrt( ans )
  ans = CheckPower( ans )
  print(ans+"\n")
  
def ThirdOrderDE( a, b, c, d ) :                                                       
  x = symbols('x')
  y = Function('y')
  
  ode = a*diff( y(x), x, 3 ) + b*diff(y(x),x,2) +  c*diff(y(x),x) + d*y(x)
  ans = str(dsolve( ode, y(x) ))
  ans = ans.replace( "Eq(y(x), ", "" )
  ans = "y=" + ans
  ans = CheckSqrt( ans )
  ans = CheckPower( ans )
  print(ans+"\n")
 
def Count3( value, a, b, c, d ) :
    x = value.index( "D3y" )
    
    if ( x == 0 ) :
      a = 1
    elif ( value.find( "-D3y" ) != -1 ) :
      a = -1
    else :
      temp = value[0:x-1]
      a = int( temp )
    
    if ( value.find( "D2y" ) != -1 ) :
      store = x
      x = value.index( "D2y" )
        
      if ( x == store + 4 ) :
        if ( value.find( "-D2y" ) != -1 ) :
          b = -1 
        else :
          b = 1
      else :
        temp = value[store+3:x-1]
        b = int( temp )

    if ( value.find("Dy") != -1 ) :
      store = x
      x = value.index( "Dy" )
    
      if ( x == store + 4 ) :
        if ( value.find( "-Dy" ) != -1 ) :
          c = -1 
        else :
          c = 1
      else :
        temp = value[store+3:x-1]
        c = int( temp )
    else :
      x = x + 1     #lack Dy e.g., D3y+D2y+y=0, D3y+y=0 

    if ( value.rfind( "y" ) != -1 ) :    
      store = x
      x = value.rindex( "y" )

      if ( value[x-1] == '*' or value[x-1] == '+' or value[x-1] == '-' ) :    
        if ( x == store + 3 ) :
          if ( value.find( "-y" ) != -1 ) :
            d = -1
          else :
            d = 1
        else :
          temp = value[store+2:x-1]
          d = int( temp )
    
    #print(a, b, c, d)
    return a, b, c, d

def Count2( value, a, b, c ) :
    x = value.index( "D2y" )
    
    if ( x == 0 ) :
      a = 1
    elif ( value.find( "-D2y" ) != -1 ) :
      a = -1
    else :
      temp = value[0:x-1]
      a = int( temp )
    
    if ( value.find("Dy") != -1 ) :
      store = x
      x = value.index( "Dy" )
    
      if ( x == store + 4 ) :
        if ( value.find( "-Dy" ) != -1 ) :
          b = -1 
        else :
          b = 1
      else :
        temp = value[store+3:x-1]
        b = int( temp )
    else :
      x = x + 1     #lack Dy e.g., D2y+y=0      

    if ( value.rfind("y") != -1 ) :    
      store = x
      x = value.rindex( "y" )
    
      if ( value[x-1] == '*' or value[x-1] == '+' or value[x-1] == '-' ) :
        if ( x == store + 3 ) :
          if ( value.find( "-y" ) != -1 ) :
            c = -1
          else :
            c = 1
        else :
          temp = value[store+2:x-1]
          c = int( temp )
    
    #print(a, b, c)
    return a, b, c

def Analysis( list ) :
  for value in list :  
    error = False 
    D3y = D2y = Dy = 0   
    
    if ( value.find( "=0" ) == -1 ) :     #Nonhomogeneous
      error = True
    
    D3y = value.count( "D3y" )
    D2y = value.count( "D2y" )
    Dy = value.count( "Dy" )
    
    if ( D3y == 0 and D2y == 0 ):     #n!=2or3
      error = True
        
    if ( D3y > 1 or D2y > 1 or Dy > 1  ) :     #duplicate
      error = True
      
    if ( error ) :
      print( "Not Supported!\n" )
    else :     #correct sentence
      a = b = c = d = 0
      
      if ( D3y == 1 ) :
        a, b, c, d = Count3( value, a, b, c, d )
        ThirdOrderDE( a, b, c, d )
      else :
        a, b, c = Count2( value, a, b, c )
        SecondOrderDE( a, b, c )

if __name__ == '__main__' :
  list = []
  ReadInput( list )
  Analysis( list )