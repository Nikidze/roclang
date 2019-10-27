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
    for( int i=0; i<arr.value.size()-1; ++i)
        out << arr.value[i].value << ',' << ' ';
    out << arr.value[arr.value.size()-1].value << endl;

    return out;
}