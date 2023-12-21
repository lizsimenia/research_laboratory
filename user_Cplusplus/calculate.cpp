#include <iostream>
#include <vector>
#include <random>
#include <chrono>

using namespace std;

pair<double, vector<int>> generate_mass(int num, string type_data, string operation) {
    double start_time, end_time;
    vector<int> mass;

    if (type_data == "int") {
        start_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();

        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<int> dis(2, 3);
        for (int i = 0; i < num; i++) {
            mass.push_back(dis(gen));
        }

        end_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
    }
    else if (type_data == "unsigned int")
    {
        start_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();

        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<unsigned int> dis(2, 3);
        for (int i = 0; i < num; i++) {
            mass.push_back(dis(gen));
        }

        end_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
    }

    else if (type_data == "long")
    {
        start_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();

        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<long> dis(2, 3);
        for (int i = 0; i < num; i++) {
            mass.push_back(dis(gen));
        }

        end_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
    }

    else if (type_data == "unsigned long")
    {
        start_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();

        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<unsigned long> dis(2, 3);
        for (int i = 0; i < num; i++) {
            mass.push_back(dis(gen));
        }

        end_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
    }

    else if (type_data == "float")
    {
        start_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();

        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<float> dis(2, 3);
        for (int i = 0; i < num; i++) {
            mass.push_back(dis(gen));
        }

        end_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
    }

    else if (type_data == "double")
    {
        start_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();

        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<double> dis(2, 3);
        for (int i = 0; i < num; i++) {
            mass.push_back(dis(gen));
        }

        end_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
    }

    return make_pair(end_time - start_time, mass);
}

int main()
{
    pair<double, vector<int>> result = generate_mass(100, "int", "+");

    double mass = result.first;
    vector<int> vector_int = result.second;

    cout << "Mass: " << mass << endl;
    cout << "Vector int: {";
    for (int x : vector_int) {
        cout << x << ", ";
    }
    cout << "}" << endl;
    return 0;
}
