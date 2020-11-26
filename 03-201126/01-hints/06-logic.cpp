#include <cassert>
#include <iostream>

bool bar() {
    return false;
}

bool foo() {
    std::cout << "foo()\n";
    assert(false);
}

int main() {
    if (bar() && foo()) {
        std::cout << "WTF?\n";
    } else {
        std::cout << "Nice\n";
    }
}
