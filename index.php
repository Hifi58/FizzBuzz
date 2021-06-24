<?php
$number= -1;

    while(++$number < 101){ 
        
    
        if (!($number%3) && !($number%5)){
           echo "Fizzbuzz <br/>";
        }elseif(!($number%5)){
            echo "buzz <br/>";
        }elseif(!($number%3)) {
            echo "fizz <br/>";
        }else{
            echo $number."<br/>";
        };
        
    }