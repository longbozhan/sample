cmake_minimum_required(VERSION 3.1.0)
project(casetest)

# Now simply link against gtest or gtest_main as needed.
add_executable(casetest case_test.cpp)
target_link_libraries(casetest gtest_main) #gtest_main提供了程序入口点，意味着不需要写main函数，gtest没有
enable_testing()