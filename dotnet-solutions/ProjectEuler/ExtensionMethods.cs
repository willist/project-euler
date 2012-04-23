using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ProjectEuler
{
    public static class ExtensionMethods
    {
        public static IEnumerable<int> Factors(this int number)
        {
            var sqrt = Math.Sqrt(number);
         
            // find all factors smaller than or equal to the sqrt of the number being factored
            var left_factors = Enumerable.Range(1, Convert.ToInt32(sqrt))
                .Where(x => (number % x == 0));

            // using smaller factors, find factors larger than sqrt
            var right_factors = left_factors
                .Reverse()
                .Where(x => x != sqrt)
                .Select(x => number / x);

            return left_factors.Concat(right_factors);
        }

        public static IEnumerable<long> PrimeFactors(this long number)
        {
            var current_number = number;
            foreach (var prime in Utilities.Primes())
            {
                if (current_number == 1)
                {
                    break;
                }

                while (current_number % prime == 0)
                {
                    yield return prime;
                    current_number /= prime;
                }
            }
        }
    }
}
