using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ProjectEuler
{
    public static class IntExtensions
    {
        public static IEnumerable<int> Factors(this int number)
        {
            var sqrt = Convert.ToInt32(Math.Sqrt(number));
            var left_factors = Enumerable.Range(1, sqrt)
                .Where(x => (number % x == 0));
            var right_factors = left_factors.Reverse().Where(x => x != sqrt).Select(x => number / x);

            return left_factors.Concat(right_factors);
        }
    }
}
