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

        public static bool Is_Palindrome(int value)
        {
            string s_value = Convert.ToString(value);
            string s_value_reversed = new string(s_value.Reverse().ToArray());
            return s_value.Equals(s_value_reversed);
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
    }
}
