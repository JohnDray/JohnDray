using System;

namespace joe
{
    class Program
    {
        static void Main(string[] args)
        {
            //string variable(s)
            string whosjoe = "joemama";
            string whosben = "bendover";

            //print statement not printing a line.
            Console.Write("gaminmg");
            // \n is to enetr a line.
            Console.Write(" is so epic don tyou agree? \n");

            //print statement in c# but with multiple string values
            Console.WriteLine($"Q. whos joe and whos ben?. A. {whosjoe} and {whosben}!!!");

            //print statement declaring the length of each string variables.
            Console.WriteLine($"ben dover has {whosben.Length} letters, and joe mama has {whosjoe.Length} words.");

            //print statement in c# but with multiple values
            Console.WriteLine("whos joe? " + whosjoe);

            //print statement in c# with string interpolation.
            Console.WriteLine($"whos joe? {whosjoe}");





            //trimming

            string notaninsult = "     no one likes you     ";
            Console.WriteLine($"[{notaninsult}]");

            string trimmedGreeting = notaninsult.TrimStart();
            Console.WriteLine($"[{trimmedGreeting}]");

            trimmedGreeting = notaninsult.TrimEnd();
            Console.WriteLine($"[{trimmedGreeting}]");

            trimmedGreeting = notaninsult.Trim();
            Console.WriteLine($"[{trimmedGreeting}]");

            //replacing
            string sayHello = "No thanks";
            Console.WriteLine(sayHello);
            string actuallysaidhello = sayHello.Replace("No", "sure bro, please say");
            Console.WriteLine(actuallysaidhello);

            //upper to lower
            Console.WriteLine(sayHello.ToUpper());
            Console.WriteLine(sayHello.ToLower());

            //searching strings
            string bangers = "Never gonna give you up";

            Console.WriteLine(bangers.Contains("give"));
            Console.WriteLine(bangers.Contains("always"));
            Console.WriteLine(bangers.StartsWith("gonna"));

        }
    }
}
