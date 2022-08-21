#SP contains which RAM location it is
#SP starts with 256
#LCL starts with 1015
#arithmetic
g = open("vmFile.vm", "r")
toAssembly = "vmFile"
f = open(toAssembly + ".asm", "w+")
def local(vm):
    #since it can only be either push/pop for segment lcl
    #common to push and pop
    #addr=LCL+i
    words = vm.split()
    i = words[2]
    linesa = '@1\nD=M\n@addr\nM=D\n' + '@' + i + '\nD=A\n@addr\nM=M+D'
    #append asm code lines to file here
    f.write(linesa + '\n')
    #if pop
    if vm.find('pop') != -1:
        #execute pop code
        #SP--
        linesb = '@SP\nM=M-1'
        f.write(linesb + '\n')
        #*addr=*SP
        linesc = '@addr\nA=M\nD=M\n@SP\nA=M\nM=D\n'
        f.write(linesc + '\n')
    if vm.find('push') != -1:
        #execute push code
        #*SP=*addr
        linesb = '@addr\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP'
        f.write(linesb + '\n')
        #SP++
        linesc = 'M=M+1'
        f.write(linesc + '\n')
def argument(vm):
    words = vm.split()
    i = words[2]
    linesa = '@ARG\nD=M\n@addr\nM=D\n' + '@' + i + '\nD=A\n@addr\nM=M+D'
    #append asm code lines to file here
    f.write(linesa + '\n')
    #if pop
    if vm.find('pop') != -1:
        #execute pop code
        #SP--
        linesb = '@SP\nM=M-1'
        f.write(linesb + '\n')
        #*addr=*SP
        linesc = '@SP\nA=M\nD=M\n@addr\nA=M\nM=D' #In pop it pops it to addr
        f.write(linesc + '\n')
    if vm.find('push') != -1:
        #execute push code
        #*SP=*addr
        linesb = '@addr\nA=M\nD=M\n@SP\nA=M\nM=D'
        f.write(linesb + '\n')
        #SP++
        linesc = 'M=M+1'
        f.write(linesc + '\n')
#S
def this(vm):
    words = vm.split()
    i = words[2]
    linesa = '@THIS\nD=M\n@addr\nM=D\n' + '@' + i + '\nD=A\n@addr\nM=M+D'
    #append asm code lines to file here
    f.write(linesa + '\n')
    #if pop
    if vm.find('pop') != -1:
        #execute pop code
        #SP--
        linesb = '@SP\nM=M-1'
        f.write(linesb + '\n')
        #*addr=*SP
        linesc = '@SP\nA=M\nD=M\n@addr\nA=M\nM=D'
        f.write(linesc + '\n')
    if vm.find('push') != -1:
        #execute push code
        #*SP=*addr
        linesb = '@addr\nA=M\nD=M\n@SP\nA=M\nM=D'
        f.write(linesb + '\n')
        #SP++
        linesc = '@SP\nM=M+1'
        f.write(linesc + '\n')
def that(vm):
    words = vm.split()
    i = words[2]
    linesa = '@THAT\nD=M\n@addr\nM=D\n' + '@' + i + '\nD=A\n@addr\nM=M+D'
    #append asm code lines to file here
    f.write(linesa + '\n')
    #if pop
    if vm.find('pop') != -1:
        #execute pop code
        #SP--
        linesb = '@SP\nM=M-1'
        f.write(linesb + '\n')
        #*addr=*SP
        linesc = '@SP\nA=M\nD=M\n@addr\nA=M\nM=D'
        f.write(linesc + '\n')
    if vm.find('push') != -1:
        #execute push code
        #*SP=*addr
        linesb = '@addr\nA=M\nD=M\n@SP\nA=M\nM=D'
        f.write(linesb + '\n')
        #SP++
        linesc = 'M=M+1'
        f.write(linesc + '\n')
def constant(vm):
    words = vm.split()
    i = words[2]
    #only push constant command
    linesa = '@' + i + '\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1'
    f.write(linesa + '\n')
def static(vm):
    words = vm.split()
    #only pop
    i = words[2]
    if (vm.find('pop') != -1):
        #we don't use a variable addr here because foo.n will
        #automatically go to the variable section in RAM (16
        #register onwards); unlike local, etc, where we wanted
        #it to go to a specific place like 1015 + i, which is
        #why we stored the latter value in a var addr.
        linesa = '@SP\nM=M-1\nA=M\nD=M\n@' + toAssembly + '.' + i + '\nM=D'
        f.write(linesa + '\n')
    if (vm.find('push') != -1):
        linesa = '@' + toAssembly + '.' + i + '\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
        f.write(linesa + '\n')
def temp(vm):
    words = vm.split()
    #common code for pop and push
    #addr = 5 + i
    i = words[2]
    linesa = '@5\nD=A\n@addr\nM=D\n@' + i + '\nD=A\n@addr\nM=M+D'
    f.write(linesa + '\n')
    #if pop
    if (vm.find('pop') != -1):
        #SP--
        linesb = '@SP\nM=M-1'
        f.write(linesb + '\n')
        #*addr=*SP
        linesc = '@SP\nA=M\nD=M\n@addr\nA=M\nM=D'
        f.write(linesc + '\n')
    if (vm.find('push') != -1):
        #*SP=*addr
        linesb = '@addr\nA=M\nD=M\n@SP\nA=M\nM=D'
        f.write(linesb + '\n')
        #SP++
        linesc = '@SP\nM=M+1'
        f.write(linesc + '\n')
def pointer(vm):
    f.write(vm + '\n')
    words = vm.split()
    #pop
    if (vm.find('pop') != -1):
        #SP--
        linesa = '@SP\nM=M-1'
        f.write(linesa + '\n')
        #THIS/THAT=*SP corresponding to 0/1
        if (vm.find('0') != -1):
            linesb = '@THIS\nD=M\n@SP\nA=M\nM=D'
            f.write(linesb + '\n')
        if (vm.find('1') != -1):
            linesb = '@THAT\nD=M\n@SP\nA=M\nM=D'
            f.write(linesb + '\n')
    #push
    if (vm.find('push') != -1):
        #*SP=THIS/THAT
        if (vm.find('0') != -1):
            linesa = '@THIS\nD=M\n@SP\nA=M\nM=D'
            f.write(linesa + '\n')
        if (vm.find('1') != -1):
            linesa = '@THAT\nD=M\n@SP\nA=M\nM=D'
            f.write(linesa + '\n')
        #SP++
        linesb = '@SP\nM=M+1'
        f.write(linesb + '\n')
def arithmetic(vm):
    #printing = vm
    f.write(vm + '\n')
    #f.write(printing+'\n')
    if (vm.find('add') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D'
        f.write(linesa + '\n')
    if (vm.find('sub') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D'
        f.write(linesa + '\n')
def logic(vm):
    f.write(vm + '\n')
    if (vm.find('neg') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\nD=M+D\n@SP\nA=M\nM=M-D'
        f.write(linesa + '\n')
    if (vm.find('eq') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\nM=-1\n@YES\nD;JEQ\n@NO\n0;JMP\n(YES)\n@SP\nA=M\nM=0\n(NO)'
        f.write(linesa + '\n')
    if (vm.find('gt') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\nM=-1\n@SP0\nD;JGT\n@SP1\n0;JMP\n(SP0)\n@SP\nA=M\nM=0\n(SP1)'
        f.write(linesa + '\n')
    if (vm.find('lt') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D-M\nM=-1\n@LT\nD;JGT\n@NLT\n0;JMP\n(LT)\n@SP\nA=M\nM=0\n(NLT)'
        f.write(linesa + '\n')
    if (vm.find('and') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M'
        f.write(linesa + '\n')
    if (vm.find('or') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M'
        f.write(linesa + '\n')
    if (vm.find('not') != -1):
        linesa = '@SP\nM=M-1\n@SP\nA=M\nD=M\nM=!D'
        f.write(linesa + '\n')
f = open(toAssembly + ".asm", "a+")
lines = g.readlines()
f.write('@256\nD=A\n@0\nM=D'+'\n')
f.write('@300\nD=A\n@1\nM=D'+'\n')
f.write('@400\nD=A\n@2\nM=D'+'\n')
f.write('@3000\nD=A\n@3\nM=D'+'\n')
f.write('@3010\nD=A\n@4\nM=D'+'\n')
for l in lines:
    if (l.find('local') != -1):
        local(l)
    if (l.find('constant') != -1):
        constant(l)
    if (l.find('temp') != -1):
        temp(l)
    if (l.find('pointer') != -1):
        pointer(l)
    if (l.find('this') != -1):
        this(l)
    if (l.find('that') != -1):
        that(l)
    if (l.find('static') != -1):
        static(l)
    if (l.find('argument') != -1):
        argument(l)
    if (l.find('add') != -1):
        arithmetic(l)
    if (l.find('sub') != -1):
        arithmetic(l)
    if (l.find('neg') != -1):
        logic(l)
    if (l.find('eq') != -1):
        logic(l)
    if (l.find('gt') != -1):
        logic(l)
    if (l.find('lt') != -1):
        logic(l)
    if (l.find('and') != -1):
        logic(l)
    if (l.find('or') != -1):
        logic(l)
    if (l.find('not') != -1):
        logic(l)

f.write('(END)\n@END\n0;JMP' + '\n')
f.close()
