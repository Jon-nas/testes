class pessoa{

    constructor(nome, sobreNome){
        this.nome = nome;
        this.sobreNome = sobreNome;
    }

    falar(){
        console.log('Olá ' + this.nome);
    }

    get nomeCompleto(){
        console.log('Olá ' + this.nome +' '+ this.sobreNome);
    }
}

p1 = new pessoa('Fabio', 'Silva');
p1.falar();
p1.nomeCompleto;



class dispositivoEletronico{
    constructor(nome){
        this.nome = nome;
        this.ligado = false;
    }

    ligar(){
        if(this.ligado){
            console.log('Já está ligado')
            return;
        }
        this.ligado = true;
    }
}

// Herança

class smartPhone extends dispositivoEletronico{
    constructor(nome, cor, modelo){
        super(nome);
        this.cor = cor;
        this.modelo = modelo;
    }
}

var s1 = new smartPhone('Samsung', 'Preto', 'A71');
console.log(s1);
s1.ligar();
s1.ligar();