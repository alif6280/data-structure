#include<bits/stdc++.h>
using namespace std;

class Stack {
public:
    vector<int> x;

    void push(int v) { x.push_back(v); }

    int pop() {
        int temp = x.back();
        x.pop_back();
        return temp;
    }

    int top() { return x.back(); }

    bool empty() { return x.empty(); }

    int size() { return x.size(); }

    void print() {
        cout << "Stack Elements: ";
        for(int v : x) cout << v << " ";
        cout << endl;
    }
};

int main() {
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.push(50);

    s.print();
    cout << "Top Element : " << s.top() << endl;

    cout << "Popped : " << s.pop() << endl;
    cout << "After popped : ";
    s.print();

    s.x.insert(s.x.begin() + 1, 99);
    cout << "Inserted element : ";
    s.print();

    s.x.erase(s.x.begin() + 2);
    cout << "Delete element : ";
    s.print();

    s.print();

    cout << "Empty ? " << (s.empty() ? "Yes" : "No") << endl;
    cout << "Size: " << s.size() << endl;
    return 0;
}
