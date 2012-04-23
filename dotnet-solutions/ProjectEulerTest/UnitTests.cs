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
            Assert.AreEqual<int>(6857, solution.Problem003());
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
        }
    }
}
