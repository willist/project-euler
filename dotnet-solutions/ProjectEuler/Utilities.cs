using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ProjectEuler
{
    public class Utilities
    {
        public static IEnumerable<int> Fibonacci()
        {
            int first = 0;
            int second = 1;

            yield return first;
            yield return second;

            while (true)
            {
                int new_value = first + second;
                yield return new_value;

                first = second;
                second = new_value;
            }
        }

        public static IEnumerable<int> TriangleNumbers()
        {
            var current = 0;
            foreach (var item in Utilities.NumberGenerator(1))
            {
                current += item;
                yield return current;
            }
        }

        public static bool Is_Palindrome(int value)
        {
            string s_value = Convert.ToString(value);
            string s_value_reversed = new string(s_value.Reverse().ToArray());
            return s_value.Equals(s_value_reversed);
        }
        
        public static IEnumerable<int> Primes()
        {
            var ints = Enumerable.Range(2, Int32.MaxValue - 1);
            return ints.Where(x => x.Factors().Take(2).Max() == x);
        }

        public static IEnumerable<Tuple<int, int>> CartesianProduct(IEnumerable<int> iter1, IEnumerable<int> iter2)
        {
            foreach (var item1 in iter1)
            {
                foreach (var item2 in iter2)
                {
                    yield return Tuple.Create<int, int>(item1, item2);
                }
            }
        }

        public static IEnumerable<Tuple<int, int, int>> CartesianProduct(IEnumerable<int> iter1, IEnumerable<int> iter2, IEnumerable<int> iter3)
        {
            foreach (var item1 in iter1)
            {
                foreach (var item2 in iter2)
                {
                    foreach (var item3 in iter3)
                    {
                        yield return Tuple.Create<int, int, int>(item1, item2, item3);
                    }
                }
            }
        }
        
        public static IEnumerable<int> NumberGenerator(int start = 0, int step = 1)
        { 
            while (true)
            {
                yield return start;
                start += step;
            }
        }
    }
}
