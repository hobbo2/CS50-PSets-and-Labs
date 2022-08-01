// Event listener for q1 & 3
document.addEventListener('DOMContentLoaded',function()
{
    let answer = document.querySelector('#correct');
    let notAnswer = document.querySelectorAll('.incorrect');
    let message = document.querySelector('#message');
    let right = document.querySelector('#right');
    let wrong = document.querySelectorAll('.wrong');
// Q1
    answer.addEventListener('click',function()
    {
        answer.style.backgroundColor = 'green';
        message.innerHTML = 'Correct';
    })
    for(let i = 0; i < notAnswer.length; i++)
    {
        notAnswer[i].addEventListener('click',function()
        {
            notAnswer[i].style.backgroundColor = 'red';
            message.innerHTML = 'Incorrect, Try again';
        })

    }
    // Q3
    right.addEventListener('click',function(){
        right.style.backgroundColor = 'green'
        p3message.innerHTML = 'Correct';
    })
    for( let i = 0; i < wrong.length; i++){
        wrong[i].addEventListener('click',function(){
            wrong[i].style.backgroundColor = 'red';
            p3message.innerHTML = 'Incorrect, Try again';
        })
    }
    // Event listener for Q2
    document.querySelector('#p2Button').addEventListener('click',function()
    {
        let input = document.querySelector('input');
        if (input.value == 'Costa Rica')
        {
            p2Message.innerHTML = 'Correct!';
            input.style.backgroundColor = 'green';
        }
        else {
            p2Message.innerHTML = 'Incorrect! Try Again';
            input.style.backgroundColor = 'red';
        }
    })
    document.querySelector('#p4Button').addEventListener('click',function()
    {
        let n = document.querySelector('#n');
        if (n.value == 'USA')
        {
            p4Message.innerHTML = 'Correct!';
            n.style.backgroundColor = 'green';
        }
        else {
            p4Message.innerHTML = 'Incorrect! Try Again';
            n.style.backgroundColor = 'red';
        }
    })

  

})
;