﻿using System;
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
            return Enumerable.Range(0, 1000)
                .Where(x => (x % 3 == 0 || x % 5 == 0))
                .Sum();
        }

        /// <summary>
        /// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
        ///     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
        ///
        /// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
        /// </summary>
        /// <returns></returns>
        public int Problem002()
        {
            return Utilities.Fibonacci()
                .TakeWhile<int>(value => (value < 4000000))
                .Where<int>(value => (value % 2 == 0))
                .Sum();
        }

        /// <summary>
        /// The prime factors of 13195 are 5, 7, 13 and 29.
        ///
        ///What is the largest prime factor of the number 600851475143 ?
        /// </summary>
        /// <returns></returns>
        public long Problem003()
        {
            var number = 600851475143;
            return number.PrimeFactors().Max();
        }

        /// <summary>
        /// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
        ///
        /// Find the largest palindrome made from the product of two 3-digit numbers.
        /// </summary>
        /// <returns></returns>
        public int Problem004()
        {
            Func<Tuple<int, int>, int> product = input => input.Item1 * input.Item2;
            
            return Utilities.CartesianProduct(Enumerable.Range(0, 1000), Enumerable.Range(0, 1000))
                .Select(product)
                .Where(Utilities.Is_Palindrome)
                .Max();
        }

        /// <summary>
        /// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

        /// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
        /// </summary>
        /// <returns></returns>
        public int Problem005()
        {
            return Utilities.NumberGenerator(1)
                .Where(x => 
                    Enumerable.Range(1, 20).All(y => x % y == 0))
                .First();
        }
        
        /// <summary>
        /// The sum of the squares of the first ten natural numbers is,
        /// 1^2 + 2^2 + ... + 10^2 = 385
        /// 
        /// The square of the sum of the first ten natural numbers is,
        /// (1 + 2 + ... + 10)^2 = 55^2 = 3025
        /// 
        /// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
        ///
        /// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
        /// </summary>
        /// <returns></returns>
        public int Problem006()
        {
            var input = 100;
            var sumOfSquares = Enumerable.Range(1, input).Select(x => x * x).Sum();
            var squareOfSum = Convert.ToInt32(Math.Pow(Enumerable.Range(1, input).Sum(), 2));
            return Math.Abs(squareOfSum - sumOfSquares);
        }

        /// <summary>
        /// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
        ///
        /// What is the 10,001st prime number?
        /// </summary>
        /// <returns></returns>
        public int Problem007()
        {
            return Utilities.Primes().Skip(10000).First();
        }

        /// <summary>
        /// Find the greatest product of five consecutive digits in the 1000-digit number.
        /// 
        /// 73167176531330624919225119674426574742355349194934
        /// 96983520312774506326239578318016984801869478851843
        /// 85861560789112949495459501737958331952853208805511
        /// 12540698747158523863050715693290963295227443043557
        /// 66896648950445244523161731856403098711121722383113
        /// 62229893423380308135336276614282806444486645238749
        /// 30358907296290491560440772390713810515859307960866
        /// 70172427121883998797908792274921901699720888093776
        /// 65727333001053367881220235421809751254540594752243
        /// 52584907711670556013604839586446706324415722155397
        /// 53697817977846174064955149290862569321978468622482
        /// 83972241375657056057490261407972968652414535100474
        /// 82166370484403199890008895243450658541227588666881
        /// 16427171479924442928230863465674813919123162824586
        /// 17866458359124566529476545682848912883142607690042
        /// 24219022671055626321111109370544217506941658960408
        /// 07198403850962455444362981230987879927244284909188
        /// 84580156166097919133875499200524063689912560717606
        /// 05886116467109405077541002256983155200055935729725
        /// 71636269561882670428252483600823257530420752963450
        /// </summary>
        /// <returns></returns>
        public int Problem008()
        {
            var big_num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
            return big_num.Chunkify(5)
                .Select(chunk => 
                    chunk.Select(piece => Convert.ToInt32(piece.ToString())).Product())
                .Max();
        }

        /// <summary>
        /// A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
        ///
        /// a2 + b2 = c2
        /// For example, 32 + 42 = 9 + 16 = 25 = 52.
        ///
        /// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        /// Find the product abc.
        /// </summary>
        /// <returns></returns>
        public int Problem009()
        {
            Func<Tuple<int, int, int>, bool> isPythagorean = delegate(Tuple<int, int, int> x)
            {
                return (Math.Pow(x.Item1, 2) + Math.Pow(x.Item2, 2) == Math.Pow(x.Item3, 2));
            };

            return Utilities.CartesianProduct(Enumerable.Range(1, 1000), Enumerable.Range(1, 1000), Enumerable.Range(1, 1000))
                .Where(x => (x.Item1 + x.Item2 + x.Item3) == 1000)
                .Where(isPythagorean)
                .Select(x => new List<int> { x.Item1, x.Item2, x.Item3 }.AsEnumerable().Product())
                .First();

        }

        /// <summary>
        /// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

        /// Find the sum of all the primes below two million.
        /// </summary>
        /// <returns></returns>
        public long Problem010()
        {
            return Utilities.Primes().Select(x => (long)x).TakeWhile(x => x < 2000000).Sum();
        }

        /// <summary>
        /// The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
        /// 
        /// 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
        /// 
        /// Let us list the factors of the first seven triangle numbers:
        /// 
        /// 1: 1
        /// 3: 1,3
        /// 6: 1,2,3,6
        /// 10: 1,2,5,10
        /// 15: 1,3,5,15
        /// 21: 1,3,7,21
        /// 28: 1,2,4,7,14,28
        /// We can see that 28 is the first triangle number to have over five divisors.
        /// 
        /// What is the value of the first triangle number to have over five hundred divisors?
        /// </summary>
        /// <returns></returns>
        public long Problem012()
        {
            return Utilities.TriangleNumbers().Where(x => x.Factors().Count() > 500).First();
        }
    }
}
