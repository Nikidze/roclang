#include <string>
#include <sstream>
string tostr(int noString){
    std::stringstream ss;
    ss<<noString;
    std::string str;
    ss>>str;
    return str;
}
int toint(string noInt){
    istringstream iss (noInt, istringstream::in);
    int val;
    iss >> val;
    return val;
}
