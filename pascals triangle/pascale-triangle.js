let generatePascal = (result,n)=>{
    let last = result[result.length - 1]
    let newRow = new Array(last.length + 1)
    newRow[0] = 1
    newRow[newRow.length] = 1    
}

let pascal = (n)=>{
    let result = [[1],[1,1]]
    if(n == 2) return result
    else return generatePascal(result,n)
}


console.log(pascal(5))