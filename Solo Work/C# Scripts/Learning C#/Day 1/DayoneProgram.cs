using System;

namespace FirstCscript
{
    class Program
    {
        static void Main(string[] args)
        {
        //lost video stamps, however it will be reported in the other days.
            string oldmate = "Billy";
            string oldmate2 = "Jerrisca";
            Console.WriteLine($"That oldmate {oldmate} has {oldmate.Length} letters in his name ");
            Console.WriteLine($"That oldmate {oldmate2} has {oldmate2.Length} letters in his name");

            string whoknows = "        Oi        ";
            string iknow1 = whoknows.TrimStart();
            string iknow2 = whoknows.TrimEnd();
            string iknow3 = whoknows.Trim();
            string iknow4 = whoknows.Trim();
            Console.WriteLine($"*{iknow1}*");
            Console.WriteLine($"*{iknow2}*");
            Console.WriteLine($"*{iknow3}*");
            Console.WriteLine($"*{iknow4}*");

            string oi = "oi mate";
            Console.WriteLine($"{oi}");
            oi = oi.Replace("mate", "nerd");

            oi = oi.Replace("nerd", "");

            Console.WriteLine(oi);
            Console.WriteLine(oi.ToUpper());

            string quote = "motivational words ig";
            Console.WriteLine(quote.Contains("motivational words"));
            Console.WriteLine(quote.Contains("def motivational words"));
        }
    }
}
