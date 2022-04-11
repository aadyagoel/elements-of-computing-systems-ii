//make an array of size 10 with values 1,2,3...10 and then find their sum and average 
//first we need a loop that'll run 10 times
(LOOP) //this will run 10 times
@i //arbitrary variable symbol
D=M //this will start out as 0 and then iterate
@n // this holds the amount of times to run: eg 10
D=D-M // when this is 10 - 10 (when i becomes 10) loop terminates
@GOTOAVERAGE //two different Average Label as some codes in Average loop only to be executed once
D;JEQ // if D==0 this loop terminates

//to iterate i which will also iterate to the next register in the previous segment
@i
M=M+1
D=M
@arr //register: 18 (this will hold predefined value 20 so that the values 1,2,3 can be stored in RAM[20,21..] 
A=D+M // the register where iterations of i will be stored; M is given by arr above and D is given by value of  i
M=D //here, the reason variable arr is after i and is defined by M instead of D is because in last line M=D we want
//this to be equal to 1,2,3... but we can't define it like M=M (like i was M in Q1); this is because in Q1 a fixed value
//20 had to be stored in register 18,19; simply put: the variable whose value needs to be in Register 18,19 is given by D. 

//sum
@sum // this will automatically go to register 30
// we can do this 2 ways: either add the A=D+M registers or add i, but since i is technically only the iterator
// and not the actual register, we should try to do it with A=D+M; but that's the same thing too because A is also being
//defined as A=D+M and D here is value of i 
M=M+D //D is defined as value of i above 

@LOOP
0;JMP //this loop runs infinitely until the END condition is true

//average after sum is done
(GOTOAVERAGE)
@sum
D=M
@total //register 20
M=D
(AVERAGE)
@n
D=M
@total //register 20
M=M-D
D=M
@31 //register 31; incase it isnt case sensitive; for some reason it goes to register 21 so instead of variable, made register direct
M = M+1
@END
D;JLT //when D is less than 0, which means 1 round will happen (1 extra -10)
@AVERAGE
0;JMP

//end loop
(END)
@END
0;JMP 


 

