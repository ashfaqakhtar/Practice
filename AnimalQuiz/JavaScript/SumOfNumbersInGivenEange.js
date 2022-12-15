var start = parseInt(prompt("Enter the Range\nStart from :  "))
var end = parseInt(prompt("End :  "))
var sum=0
for(var i=start;i<=end;i++){
    sum=sum+i;
}
document.write("sum = ",sum);