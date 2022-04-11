// Subtract 2 numbers 
// RAM[2] = RAM[0] - RAM[1]
@0 // first register 
D=M 
@1 // @0 - @1 
D=M-D
@2 // store the answer in @2 
M=D
@6 // infinite loop that to end; it goes to line 6 and 7 over and over
0;JMP 
 