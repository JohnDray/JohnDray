using System;

namespace joe
{
    class Program
    {
        static void Main(string[] args)
        {
            //interger
            int a = 3;
            int b = 4;
            int aa = 2;

            //integer math showcasing basics
            int c = a * b;
            int d = a - b;
            int e = a + b;
            int f = a / b;
            int g = a + b * (c / d);
            Console.Write($"{c}\n{d}\n{e}\n{f}\n");
            Console.WriteLine(g);

            //modulo op
            c = (a + b) % aa;
            Console.WriteLine("quotient: "+ c);
            c = (a+ b)/ aa;
            Console.WriteLine("remainder: " + c);

            //int min/max values
            int max = int.MinValue;
            int min = int.MinValue;
            Console.WriteLine($"Int max is {max} and int min is {min}");

            //doubles
            double dec = 2.5;
            double num = 3.0;
            double a1 = dec + num;
            double dmax = double.MaxValue;
            double dmin = double.MinValue;
            Console.WriteLine(a1);
            Console.WriteLine($"double max is {dmax} and double min is {dmin}");

            //decimals are smaller but more accurate then doubles

            decimal demax = decimal.MinValue;
            decimal demin = decimal.MinValue;
            //M indicates that its a decimal.
            decimal a2 = 1.0M;
            decimal b2 = 3.0M;

            double a3 = 1.0;
            double b3 = 3.0;

            Console.WriteLine(a3 / b3);

            Console.WriteLine(a2 / b2);


            Console.WriteLine($"decimal max is{demax} and decimal min is {demin}");

        }
    }
}
