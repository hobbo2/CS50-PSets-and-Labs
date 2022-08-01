document.addEventListener('DOMContentLoaded',function()
{
    let answer = document.querySelector('#correct');
    let notAnswer = document.querySelectorAll('.incorrect');
    let message = document.querySelector('#message');

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
            message.innerHTML = 'Incorrect';
        })

    }
    document.querySelector('#p2Button').addEventListener('click',function()
    {
        let input = document.querySelector('input');
        if (input.value == 'Costa Rica')
        {
            p2Message.innerHTML = 'Correct!';
            input.style.backgroundColor = 'green';
        }
        else {
            p2Message.innerHTML = 'Incorrect!';
            input.style.backgroundColor = 'red';
        }
    })
});