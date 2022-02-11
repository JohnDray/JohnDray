using System;

namespace FirstCscript
{
    class Program2
    {
        static void Main(string[] args)
        {
            // video 5
            int a = 666;
            int b = 2;
            int c = a + b * 6 * 87;
            int d = (8989 * 20 - 21 + 1) / 2;
            Console.WriteLine($"{c}\n{d}");

            // video 6

            int a2 = 7;
            int b2 = 4;
            int d2 = (a2 + b2) / 3;
            int e2 = (a2 + b2) % 3;
            Console.WriteLine($"d = {d2}\ne = {e2}");

            // Max of ints. (Something 2 billion)
            int Intmax = int.MaxValue;
            int Intmin = int.MinValue;

            Console.WriteLine($"The int max is {Intmax} and the int min is " +
                $"{Intmin}");

            //Can go over max
            double Doublemax = double.MaxValue;
            double Doublemin = double.MinValue;

            Console.WriteLine($"The double max is {Doublemax} and the int min is " +
                $"{Doublemin}");

            double a3 = 5;
            double b3 = 4;
            double c3 = 2;
            double d3 = (a3 + b3) / c3;
            Console.WriteLine(d3);

            double fractionthing1 = 1.0 / 3.0;
            Console.WriteLine(fractionthing1);

        }
    }

}

