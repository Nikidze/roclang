class DBL {
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