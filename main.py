def caesar(code):
  abc='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  dic=[]
  ts=''
  x=0

  for i in abc:
    if x <= 25:
      new=[abc[x],abc[x+2]] #Change your degree of shift at +2
      dic.append(new)
    x+=1
  dic=dict(dic)

  code=code.lower()
  for i in code:
    if i in dic:
      ts+=dic[i]
    else:
      ts+=i
  
  return ts

code='''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

print(caesar(code))
