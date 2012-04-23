using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using ProjectEuler;

namespace ProjectEulerTest
{
    [TestClass]
    public class UnitTests
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
    }
}
