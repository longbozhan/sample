#include <iostream>

#include <gtest/gtest.h>

using namespace std;

class MyEnvironment0 : public testing::Environment {
    public:
        virtual void SetUp() {
            cout << "Global event0 : start1" << endl;
        }

        virtual void TearDown() {
            cout << "Global event0 : end" << endl;
        }
};

class MyEnvironment1 : public testing::Environment {
    public:
        virtual void SetUp() {
            cout << "Global event1 : start" << endl;
        }

        virtual void TearDown() {
            cout << "Global event1 : end" << endl;
        }
};

TEST(GlobalTest0, test0) {
    EXPECT_EQ(1, 1);
};

TEST(GlobalTest0, test1) {
    EXPECT_EQ(1, 1);
};

TEST(GlobalTest1, test0) {
    EXPECT_EQ(1, 1);
};

int main(int argc, char *argv[]) {
    testing::AddGlobalTestEnvironment(new MyEnvironment0);
    testing::AddGlobalTestEnvironment(new MyEnvironment1);

    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}