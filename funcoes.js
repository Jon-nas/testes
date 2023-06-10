var pessoa = {
    nome: 'Luiz',
    sobrenome: 'Otávio'
};

console.log(pessoa['sobrenome']);



var pessoa1 = new Object();
pessoa1.nome = 'Angela';
pessoa1.sobrenome = 'Silva';
pessoa1.falarNome = function(){
    console.log('O nome é: ' + this.nome);
}

console.log(pessoa1.nome);
pessoa1.falarNome();



function criarPessoa(nom, sobrenome){
    return (nom, sobrenome);
}

var p1 = criarPessoa('Lucas','Silva');
var p2 = criarPessoa('Arthur', 'Almeida');

console.log(p1);
console.log(p2);



function multiplicar(a, b){
    return a * b;
}

var x = multiplicar(2, 3);
console.log(x);




function funcao(a, b = 2, c = 4){
    console.log(a + b + c);
}

funcao(2, 6);




function test(...args){
    console.log(args);
}

test(2, 5, 6, 8, 9);