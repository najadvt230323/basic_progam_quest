// /*

console.log()
var mark = [30, 40, 50, 60, 70, 80, 90, 95]
console.log(mark)

len = mark.length
console.log(len)

hig = 0
low = 100

for (i = 0; i < len; i++) {
    if (mark[i]<low){low=mark[i]}
    if (mark[i]>hig){low=mark[i]}
}

console.log("highest mark =" , hig)
console.log("lowest mark =" , low)

a = mark.filter(n => n>=50)
b = mark.map(n => n+5)
c = mark.reduce((a,b) =>  { return a+b},0)

console.log(a)
console.log(b)
console.log(c)

// */
// ----------------------------------------------------------------
console.log()

let name_1 = ['najad' , 'aju' , 'ammu' , 'ajlab' , 'rashi']
console.log(name_1)

name_1.push('fida')
// name_1.('richu')

console.log(name_1)

name_1.pop()
console.log(name_1)

name_1.shift()
console.log(name_1)

console.log(name_1.includes("ammu"))
console.log(name_1.includes("fida"))

console.log(name_1.indexOf("ammu"))
console.log(name_1.indexOf("fida"))

a = name_1.slice(1,3)
console.log(a)

console.log(name_1.join(' - '))

// -----------------------------------------------------------------
/*

console.log()
let emp = [ ['najad',25000] , ['aju' ,30000] , ['fada' ,15000]]

a= emp.filter (a => a[1]>=25000)
b= emp.map (a => a[0])
c = emp.reduce((a,b) =>  { return a+b[1]},0)
d= emp.sort((a,b) => a[1]-b[1])
// e= emp.sort((a,b) => b[1]-a[1])

console.log(a)
console.log(b)
console.log(c)
console.log(d)
// console.log(e)
*/

// ------------------------------------------------------------------------