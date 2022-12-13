// FIRST TERM CALCULATIONS

var first_term = parseFloat(document.getElementById('first_fee').innerText);
var first_fix = parseFloat(document.getElementById('first_fix').innerText);
var first_loan_calci = (first_fix - first_term);


if(first_loan_calci < 0){
    document.getElementById('first_loan').innerText += "Payed Much";
} else {
    toString(first_loan_calci);
    document.getElementById('first_loan').innerText += first_loan_calci;    
}


// SECOND TERM CALCULATIONS

var second_term = parseFloat(document.getElementById('second_fee').innerText);
var second_fix = parseFloat(document.getElementById('second_fix').innerText);
var second_loan_calci = (second_fix - second_term);


if(second_loan_calci < 0){
    document.getElementById('second_loan').innerText += "Payed Much";
} else {
    toString(second_loan_calci);
    document.getElementById('second_loan').innerText += second_loan_calci;    
}


// THIRD TERM CALCULATIONS

var third_term = parseFloat(document.getElementById('third_fee').innerText);
var third_fix = parseFloat(document.getElementById('third_fix').innerText);
var third_loan_calci = (third_fix - third_term);


if(third_loan_calci < 0){
    document.getElementById('third_loan').innerText += "Payed Much";
} else {
    toString(third_loan_calci);
    document.getElementById('third_loan').innerText += third_loan_calci;    
}





console.log(first_loan_calci);