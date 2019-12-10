const a = function(number) {
    let reverse=0;           // Variable to store our reversed number.
    while(number!=0){       // Repeat the process until original number is 0.
        reverse=reverse*10+number%10;   //Shift reverse by 1 position and add last digit of number.
        number/=10;
        }      
    return reverse;    
}

console.log(a(1234));