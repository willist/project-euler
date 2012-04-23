using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ProjectEuler
{

    class Program
    {
        static void Main(string[] args)
        {
            var solutions = new Solutions();
            Console.WriteLine(String.Format("Answer to Problem 1 = {0}", solutions.Problem001()));
            Console.WriteLine(String.Format("Answer to Problem 2 = {0}", solutions.Problem002()));
            Console.WriteLine(String.Format("Answer to Problem 3 = {0}", solutions.Problem003()));
            Console.WriteLine(String.Format("Answer to Problem 4 = {0}", solutions.Problem004()));
            Console.ReadKey();
        }
    }
}
