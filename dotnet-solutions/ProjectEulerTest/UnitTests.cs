using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using ProjectEuler;

namespace ProjectEulerTest
{
    [TestClass]
    public class SolutionsUnitTests
    {
        private ProjectEuler.Solutions solution;

        [TestInitialize]
        public void Setup()
        {
            solution = new ProjectEuler.Solutions();
        }


        [TestMethod]
        public void TestProblem001()
        {
            Assert.AreEqual<int>(233168, solution.Problem001());
        }

        [TestMethod]
        public void TestProblem002()
        {
            Assert.AreEqual<int>(4613732, solution.Problem002());
        }

        [TestMethod]
        public void TestProblem003()
        {
            Assert.AreEqual<long>(6857, solution.Problem003());
        }

        [TestMethod]
        public void TestProblem004()
        {
            Assert.AreEqual<int>(906609, solution.Problem004());
        }
    }

    [TestClass]
    public class UtilitiesUnitTests
    {

        [TestMethod]
        public void TestIs_Palindrome()
        {
            Assert.IsTrue(Utilities.Is_Palindrome(101));
            Assert.IsFalse(Utilities.Is_Palindrome(100));
        }

        [TestMethod]
        public void TestPrimes()
        {
            var expected = new List<int> { 2, 3, 5, 7, 11 }.AsEnumerable();
            var observed = Utilities.Primes().Take(5);
            Assert.IsTrue(expected.SequenceEqual(observed));
        }
    }

    [TestClass]
    public class ExtensionMethodUnitTests
    {
        [TestMethod]
        public void TestFactors()
        { 
            var number = 10;
            var expected = new List<int> { 1, 2, 5, 10 }.AsEnumerable();
            var observed = number.Factors();
            Assert.IsTrue(expected.SequenceEqual(observed));

            number = 25;
            expected = new List<int> { 1, 5, 25 }.AsEnumerable();
            observed = number.Factors();
            Assert.IsTrue(expected.SequenceEqual(observed));

            number = 2;
            expected = new List<int> { 1, 2 }.AsEnumerable();
            observed = number.Factors();
            Assert.IsTrue(expected.SequenceEqual(observed));
        }
    }
}
