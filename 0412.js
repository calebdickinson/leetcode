var fizzBuzz=function(n){var x=[];for(let i=1;i<=n;i++){i%15==0?x.push("FizzBuzz"):i%5==0?x.push("Buzz"):i%3==0?x.push("Fizz"):x.push(i+"")}return x}
