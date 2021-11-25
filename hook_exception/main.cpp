#include <iostream>
#include <stdexcept>
#include <thread>

extern "C" { //加这3行代码，通过 hook __cxa_throw，直接 abort，可以避免 stack unwind。
// void __cxa_throw(void* ex, void* info, void (*dest)(void*)) { ::abort(); }
}

void func(){
    throw std::runtime_error("die");
}

int main() {
    std::thread t(func);
    t.join();
    return 0;
}
