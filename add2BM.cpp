#include <iostream>
using namespace std;
int main() {
    int A, B;
    cin >> A >> B;
    while (B != 0) {
        int carry = A & B;
        A = A ^ B;
        B = (unsigned int)carry << 1;
    }
    cout << A;
    return 0;
}
