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
            Console.WriteLine(String.Format("Answer to Problem 12 = {0}", solutions.Problem012()));
            Console.ReadKey();
        }
    }
}
