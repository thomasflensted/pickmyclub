$(document).ready(function () {

    $('.btn').click(function () {
        window.location = "questions.html";
    });

    $('.submit').click(function () {
        window.location = "result.html";
        //var clubs = [getClubs(), getClubs(), getClubs(), getClubs(), getClubs(), getClubs()];
    });

})

/*const { readFileSync, promises: fsPromises } = require('fs');

function getClubs(filename) {
    const contents = readFileSync(filename, 'utf-8');
    const arr = contents.split(/\r?\n/);
    return arr;
}*/

