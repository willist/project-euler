using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ProjectEuler
{
    /// <summary>
    /// Solutions to various Project Euler problems.
    /// </summary>
    /// <seealso cref="http://projecteuler.net"/>
    public class Solutions
    {
        /// <summary>
        /// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        /// 
        /// Find the sum of all the multiples of 3 or 5 below 1000.
        /// </summary>
        public int Problem001()
        {
            return Enumerable.Range(0, 1000).Where(x => (x % 3 == 0 || x % 5 == 0)).Sum();
        }

        public int Problem002()
        {
            return 0;
        }
    }
}
