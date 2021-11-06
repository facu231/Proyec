
package javaproyec;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
        public static void main (String[] args ) throws IOException{

InputStreamReader teclado = new InputStreamReader(System.in);
BufferedReader Tipeo = new BufferedReader(teclado);


System.out.println("Inngresa su primer numero: ");
String STRN1 = Tipeo.readLine();
var n1 = Integer.parseInt(STRN1);

boolean esPar = (n1 % 2 ) ==0;

if (esPar){

System.out.println("Numero par");

} else {
     System.out.println("Numero Inpar");

}


                
        
        

       











 }

}
