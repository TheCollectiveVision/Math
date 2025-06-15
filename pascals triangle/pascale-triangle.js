let generatePascal = (result, n) => {
    while (result.length < n) {
        let last = result[result.length - 1];
        let newRow = new Array(last.length + 1);
        newRow[0] = 1;
        newRow[newRow.length - 1] = 1;
        for (let i = 1; i < last.length; i++) {
            newRow[i] = last[i - 1] + last[i];
        }
        result.push(newRow);
    }
    return result;
}

let pascal = (n) => {
    if (n <= 0) return [];
    let result = [[1]];
    if (n === 1) return result;
    result.push([1, 1]);
    if (n === 2) return result;
    return generatePascal(result, n);
}


console.log(pascal(5))