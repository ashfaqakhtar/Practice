var a = Number(prompt("Enter First Number"));
var b = Number(prompt("Enter Second Number"));

var ch = prompt(
  "Press + for Addition\nPress - for Subtraction\nPress * for Multiplication\nPress / for Division\nPress % for Remainder\nPress ** for Power\nEnter Your Choice :  "
);

switch (ch) {
  case "+":
    document.write(`${a} + ${b} = ${a + b}`);
    break
  case "-":
    document.write(`${a} - ${b} = ${a - b}`);
    break
  case "*":
    document.write(`${a} * ${b} = ${a * b}`);
    break
  case "/":
    document.write(`${a} / ${b} = ${a / b}`);
    break
  case "%":
    document.write(`${a} % ${b} = ${a % b}`);
    break
  case "**":
    document.write(`${a} ** ${b} = ${a ** b}`);
break
default:
    document.write("Invalid Choice")
    break;
}


