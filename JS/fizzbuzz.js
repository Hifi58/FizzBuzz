for(let number = 0; number < 101; number++){
    if(number%15 == 0){
        console.log("Fizzbuss");
    }else if(number%3 == 0){
        console.log("Fizz");
    }else if(number%5 == 0){
        console.log("buzz");
    }else{
        console.log(number);
    }
}