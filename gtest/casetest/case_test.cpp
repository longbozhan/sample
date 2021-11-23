#include <iostream>

#include <gtest/gtest.h>

using namespace std;

class MyTestCase0 : public testing::Test
{
    protected:
        virtual void SetUp()
        {
            cout << "TestCase event0 : start" << endl;
        }

        virtual void TearDown()
        {
            cout << "TestCase event0 : end" << endl;
        }
};

class MyTestCase1 : public testing::Test
{
    protected:
        virtual void SetUp()
        {
            cout << "TestCase event1 : start" << endl;
        }
        virtual void TearDown()
        {
            cout << "TestCase event1 : end" << endl;
        }
};

TEST_F(MyTestCase0, test0)
{
    EXPECT_EQ(1, 1);
}

TEST_F(MyTestCase0, test1)
{
    EXPECT_EQ(1, 1);
}

TEST_F(MyTestCase1, test0)
{
    EXPECT_EQ(1, 1);
}

TEST_F(MyTestCase1, test1)
{
    EXPECT_EQ(1, 1);
}

int main(int argc, char *argv[])
{
    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}