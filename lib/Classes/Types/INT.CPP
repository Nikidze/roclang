class INT {
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