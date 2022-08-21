#create .Hack file
variable = 15
f = open("MaxL.Hack", "w+")
destt={'null':'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
#input comp
compt={'0':'101010','1':'111111','-1':'111010','D':'001100','A':'110000','!D':'001101','!A':'110001','-D':'001111','-A':'0110011','D+1':'011111','A+1':'110111','D-1':'0001110','A-1':'110010','D+A':'000010','D-A':'0010011','A-D':'000111','D&A':'000000','D|A':'010101','M':'110000','!M':'110001','-M':'110011','M+1':'110111','M-1':'110010','D+M':'000010','D-M':'010011','M-D':'000111','D&M':'000000','D|M':'010101'}
#input jump
jumpt={'null':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
#method to translate to machine code for C instruction
def Cinstruction(code):
    index=code.find(';')        #dest=comp;jmp
    maincode="111"
    if index==-1:     #null jmp
        x=code.find('=')
        dest=code[:x]
        value=code[x+1:]
        if value.find('M')!=-1:   #checking if M is present
            maincode+='1'
            p=str(compt.get(value))
            maincode+=p
            maincode+=destt.get(dest)
            maincode+='000'
        else:
            maincode+='0'
            maincode+=str(compt.get(value))
            maincode+=destt.get(dest)
            maincode+='000'
    else:
        x=code.find(';')  #jmp is present
        value=code[:x]
        jmp=code[x+1:]
        if value.find('M')!=-1:
            maincode+='1'
            maincode+=str(compt.get(value))
            maincode+='000'
            maincode+=str(jumpt.get(jmp))
        else:
            maincode+='0'
            maincode+=str(compt.get(value))
            maincode+=str(destt.get('null'))
            E=jumpt.get(jmp)
            maincode+=E
    print(maincode)
    f = open("MaxL.Hack","a+")
    f.write(maincode +'\n')
    f.close()

#method to translate to machine code for A instruction
def Ainstruction(code):
  while (1):
    code  = code[1:] #removes @sign
    f = open("MaxL.Hack","a+")
    if code == "@SP":
      mc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      f.write(mc+'\n')
    elif code == "LCL":
      mc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
      f.write(mc+'\n')
    elif code == "THIS":
      mc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
      f.write(mc+'\n')
    elif code == "THAT":
      mc = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
      f.write(mc+'\n')
    elif code == "ARG":
      mc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
      f.write(mc+'\n')
    elif code == "addr":
      mc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      f.write(mc+'\n')
    elif code == "KBD":
      mc = [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
      f.write(mc+'\n')
    elif code == "SCREEN":
      mc = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      f.write(mc+'\n')
    break 
    #extract number
    code = int(code) 
    #convert decimal to binary
    isn = [] #list that contains 2,4,8 (binary place values)
    machinecode = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while code != 0: 
        binary = 0 #binary number
        i = 0 #power of binary number 2^0, 2^1 2^i 
        while code >= binary: #when @n is greater than binary representation, go to next binary place value
            binary = 2**i
            i+=1 
        a = 2**(i-2) #save i (power) where 2^i is greater than @n
        isn.append(i-2) #-2 because we add i+=1 at end even after the loop finishes; and because the code runs until 2^i is greater (we want the last value where 2^i is less than @n)
        code = code - a
    #take i values and put in respective place value
    for j in range(0,len(isn)):
      x = isn[j] #[3, 2]
      machinecode[15-x] = 1
    machinecodestr = ''
    for e in machinecode: 
      machinecodestr += str(e)
    ''.join(machinecodestr)
    print(machinecodestr)
    #push machinecodestr line into the end of .Hack file
    f.write(machinecodestr+'\n')

#method to translate to machine code for C instruction
#def Cinstruction(code):

#actual code to check if the instruction is an A instruction or C instruction
#depending on that it executes one of the above A or C methods, and puts the translated binary machine code into a file 
def remove(string):
    return "".join(string.split())
g = open("MaxL.asm","r")
lines = g.readlines()
c = len(g.readlines())
newlist = []
for hi in lines:
  for hello in hi:
    if hello=="\n":
      newlist.append(hi.replace("\n",""))
x = 0
for l in (lines):
    if l[x] == '@':
      Ainstruction(l)
    else:
      A=remove(l)
      Cinstruction(A)
