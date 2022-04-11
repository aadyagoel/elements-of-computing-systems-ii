//make an array of size 10 with values 20 
//first we need a loop that'll run 10 times
(LOOP) //this will run 10 times
@i //arbitrary variable symbol
D=M //this will start out as 0 and then iterate
@n // this holds the amount of times to run: eg 10
D=D-M // when this is 10 - 10 (when i becomes 10) loop terminates
@END
D;JEQ // if D==0 this loop terminates

//to use the current value of i & to iterate the value 20 into the 20+ith register
@arr //variable name (stored in 18 register) // this is just variable for which register 
D=M 
@i
A=D+M //A calls new register RAM[16(D)+M] +M is of i and is the iteration
M=D //if we make RAM[arr]=20, then since we did D=M,we can do this

//to iterate i which will also iterate to the next register in the previous segment
@i
M=M+1

@LOOP
0;JMP //this loop runs infinitely until the END condition is true

(END) //if the END condition is true, it goes here and infinite loop to end
@END
0;JMP 


 

