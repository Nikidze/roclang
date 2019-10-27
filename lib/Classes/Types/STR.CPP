class STR {
public:
	string value;
	STR(string val): value(val) {};
	STR(): value("") {};
	STR& operator= (const STR &i)
	{
	    if (this == &i)
	        return *this;
	    value = i.value;
	    return *this;
	}
};
