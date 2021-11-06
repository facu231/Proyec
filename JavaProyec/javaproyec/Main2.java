package javaproyec;

public class Main2 {

    public static void main(String[] args){
/*
        Integer n = 10;
        while (n>=0)  {
            System.out.println(n);
            n--;


                         } */

   /* Integer I = 1;
    Integer Suma = 0;
    while (I<=25){
        if (I%2==0){
            Suma =Suma+I;
                System.out.println("La suma de todos los numeros Pares:"+ Suma); 
        }else{
            System.out.println("Numeros Inpares");
        }
        I++;} */
  
Integer Suma = 0;
for(Integer I = 1; I<=10; I++){
    if (I%2!=0){
        Suma = Suma +I;
        System.out.println(Suma);  
    }else{
        System.out.println("Numeros No disponible");

    }

} 





    }
}
