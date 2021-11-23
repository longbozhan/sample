#include <iostream>

#include <gtest/gtest.h>

using namespace std;

class MyTestSuite0 : public testing::Test
{
    protected:
        // 网上大部分写的是SetUpTestSuite，google后面升级版本了，改成SetUpTestCase
        // 相关讨论：https://stackoverflow.com/questions/54468799/google-test-using-setuptestsuite-doesnt-seem-to-work
        static void SetUpTestCase()
        {
            cout << "TestSuite event0 : start" << endl;
        }

        static void TearDownTestCase()
        {
            cout << "TestSuite event0 : end" << endl;
        }
};

class MyTestSuite1 : public testing::Test
{
    protected:
        static void SetUpTestCase()
        {
            cout << "TestSuite event1 : start" << endl;
        }

        static void TearDownTestCase()
        {
            cout << "TestSuite event1 : end" << endl;
        }
};

// 必须用TEST实现，实现上是拼成一个类MyTestSuite0_test0
TEST_F(MyTestSuite0, test0)
{
    EXPECT_EQ(1, 1);
}

TEST_F(MyTestSuite1, test0)
{
    EXPECT_EQ(1, 1);
}

TEST_F(MyTestSuite0, test1)
{
    EXPECT_EQ(1, 1);
}

TEST_F(MyTestSuite1, test1)
{
    EXPECT_EQ(1, 1);
}

//int main(int argc, char *argv[])
//{
//    testing::InitGoogleTEST_F(&argc, argv);
//
//    return RUN_ALL_TESTS();
//}
