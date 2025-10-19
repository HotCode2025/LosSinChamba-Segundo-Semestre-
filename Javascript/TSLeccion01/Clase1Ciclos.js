//While VIDEO 1
let contando = 0;                    
while (contando < 3){                
    console.log(`contando: ${contando}`);  // Con template literals
    contando++;                      
}
console.log("Fin del ciclo while");


//do while VIDEO 2
let conteor = 0;
do {
    console.log(`conteor: ${conteor}`);  // Con template literals
    contando++;
} while (contando < 3);
console.log("Fin del ciclo do while");


//For VIDEO 3
for (let contando = 0; contando < 3; contando++) {
    console.log(`contando: ${contando}`);  // Con template literals
}
console.log("Fin del ciclo for");


//palabras reservadas break VIDEO 4
for (let contando = 0; contando < 10; contando++)
        {if (contando % 2 === 0){   
        console.log(contando);  // meustra los números pares
        break;  
   
    }
}
console.log("Fin del ciclo for con break"); //termina el ciclo al encontrar el primer número par  


//palabras reservadas continue y Etiquetas Labels  VIDEO 5
inicio:
for (let contando = 0; contando <= 10; contando++) {
    if(contando % 2 !== 0) { 
        continue inicio;
        
    }
    console.log(contando);  0, 2, 4, 6, 8, 10
}
console.log("termina el ciclo");



// VIDEO 6 
inicio:
for (let contando = 0; contando <= 10; contando++) {
    if(contando % 2 !== 0) { 
        break inicio;
        
    }
    console.log(contando);  0, 2, 4, 6, 8, 10
}
console.log("termina el ciclo");

