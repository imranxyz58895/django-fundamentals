function stayContained() {
    var arrayOfNumbers = [1, 2, 3, 4, 5, 6];

    for (var i = 0; i < arrayOfNumbers.length; i++) {
        let value = arrayOfNumbers[i];
        console.log(value);
    }

    console.log(`Outside loop ${i}`);
}

stayContained();


function redundentRepetition() {
    var x = 'Alpha';
    // ............
    var x = 'Beta';
    // loads of code here
    var x = 'bravo'
    console.log(x);
}

redundentRepetition();