using namespace std;
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <typeinfo>


class STR {
public:
	string value;
	STR(string val): value(val) {};
	STR& operator= (const STR &i)
	{
	    if (this == &i)
	        return *this;
	    value = i.value;
	    return *this;
	}
};


class INT { // @suppress("Class has a virtual method and non-virtual destructor")
public:
	int value;
	INT(int val): value(val) {};
	INT(){
		value = 0;
	};
	INT& operator= (const INT &i)
	{
	    if (this == &i)
	        return *this;
	    value = i.value;
	    return *this;
	}
	STR to_s(){
		stringstream ss;
		ss << value;
		string str;
		ss >> str;
		return STR(str);
	}
	void add(int test){
	value+=test;
	}
};

class INT_ARR {
public:
	vector<INT> value;
	INT_ARR(vector<INT> val): value(val) {};
	INT_ARR& operator= (const INT_ARR &i)
	{
	    if (this == &i)
	        return *this;
	    value = i.value;
	    return *this;
	}
	INT& operator[] (const int index);
	friend std::ostream& operator<< (std::ostream &out, const INT_ARR &arr);
};
INT& INT_ARR::operator[] (const int index)
{
    return value[index];
}
std::ostream& operator<< (std::ostream &out, const INT_ARR &arr)
{
    for( int i=0; i<(int)arr.value.size()-1; i++)
        out << arr.value[i].value << ',' << ' ';
    out << arr.value[arr.value.size()-1].value << endl;

    return out;
}

class DBL { // @suppress("Class has a virtual method and non-virtual destructor")
public:
	double value;
	DBL(double val): value(val) {};
	DBL& operator= (const DBL &i)
	{
	    if (this == &i)
	        return *this;
	    value = i.value;
	    return *this;
	}
	STR to_s(){
		stringstream ss;
		ss << value;
		string str;
		ss >> str;
		return STR(str);
	}
};
int main(){
STR z = INT(895).to_s();
INT vasa = sqrt(INT(228)).value + INT(229).value;
return 0;
}
