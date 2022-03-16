def moveX(str):
  if len(str) < 1:
    return ""
  elif str[0] == "x":
    return moveX(str[1:]) +"x"
  else:
    return str[0]+moveX(str[1:])
    
print(moveX("hxxellowoxrld"))
