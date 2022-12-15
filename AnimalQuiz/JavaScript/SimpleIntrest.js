// Program to calculate Simple Intrest

var p =6500;
var r = 12.36;
var t = 5;

var si = p*r*t / 100
var final = p + si;
var emi = final/(t*12)

// console.log("Principle Amount : ", p)
// console.log("Total Time is: ", t, "Months")
// console.log("Given Rate is : ", r )
// console.log("calculted Simple intrest is : ", si)
// console.log("Final Amount : ", final)
// console.log("Calculated EMI : ", emi)

document.write("Principle Amount : ", p)
document.write("Total Time is: ", t, "Months")
document.write("Given Rate is : ", r )
document.write("calculted Simple intrest is : ", si)
document.write("Final Amount : ", final)
document.write("Calculated EMI : ", emi)
