//Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение.
// Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.
package HomeWork02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Task01 {
    public static void main(String[] args) {
        boolean flag = true;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while(flag){
            System.out.print("Введите дробное число: ");
            try{
                float fNumber = Float.parseFloat(reader.readLine());
                System.out.printf("Введенное число равно %f\n", fNumber);
                flag = false;
            } catch (IOException|NumberFormatException e) {
                System.out.println("Неверный ввод. Введите дробное число!!!");
            }

        }
    }
}