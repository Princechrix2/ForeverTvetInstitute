console.log('Hello World');

// The table Rows
var first = document.getElementById('first')
var second = document.getElementById('second')
var third = document.getElementById('third')
// The Student's School Fees in all Terms
var term1Fee = document.getElementById('first_fee').innerText;
var term2Fee = document.getElementById('first_term_fee').innerText;
var term3Fee = document.getElementById('first_term_fee').innerText;

// The School Fixed Fees in all terms 
var term1FixedFee = document.getElementById('first_term_fixed_fee').innerText;
var term2FixedFee = document.getElementById('second_term_fixed_fee').innerText;
var term3FixedFee = document.getElementById('third_term_fixed_fee').innerText;

// Calculations 

var TotalFixedFee = parseInt(term1FixedFee) + parseInt(term2FixedFee) + parseInt(term3FixedFee);

var TotalPaidFee = parseInt(term1Fee) + parseInt(term2Fee) + parseInt(term2Fee)

console.log(term1);


// The Magic Section 

// if (parseInt(term1Fee) != parseInt(term1FixedFee)) {
//     first.style.backgroundColor = 'red';
// } else if (parseInt(term1Fee) == parseInt(term1FixedFee)) {
//     first.style.backgroundColor = 'green';
//     first.style.color = 'white';
// }





// console.log(term2FixedFee);