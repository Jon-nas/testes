var salario = 6000;
var percentual = 10;
var aumento = 0;
var salarioComAumento = 0;

aumento = salario * percentual/100;
salarioComAumento = salario + aumento;

console.log('O salario reajustado é : ' + salarioComAumento);




var numeroInteiro = 19;
var sucessor = 88;
var antecessor = 3;

console.log('o antecessor é : ' + antecessor, ', o número inteiro é : ' + (numeroInteiro), ', e seu sucesso é : ' + (sucessor));




var custoFabrica = 40000;
var porcDist;
var porcImp;
var custoFinal;

porcDist = custoFabrica * 28/100;
porcImp = custoFabrica * 45/100;
custoFinal = custoFabrica + porcDist + porcImp;
console.log('O custo final ao consumidor é : ' + custoFinal);




var n1 = 2;
var n2 = 3;
var n3 = 5;
var mediaFinal;

mediaFinal = (n1 * 2 + n2 * 3 + n3 * 5)/10;

console.log('Media finha é : ' + mediaFinal);




var nu1 = 3;
var nu2 = 5;
var nu3 = 7;
var nu4 = 9;
var mediaPonderada;

mediaPonderada = (nu1 * 1 + nu2 * 2 + n3 * 3 + nu4 * 4);

console.log('Média ponderada é : ' + mediaPonderada);




var valor = 1000;
var valorDesconto = valor * 0.09;
var valorFinal = valor - valorDesconto;

console.log('Preço com desconto: ' + valorFinal);




var tempo = 3;
var velocidade = 80;
var distancia = tempo * velocidade;
var litros = distancia/12;

console.log('A velocidade media percorrida por litro é: ' + velocidade + 'Km/h');
console.log('O tempo gasto na viagem foi: ' + tempo + 'h');
console.log('A distancia percorrida é: ' + distancia + 'km');
console.log('Consumo de combustível foi: ' + litros + 'l/km');