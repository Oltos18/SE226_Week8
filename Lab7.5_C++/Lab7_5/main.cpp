#include <iostream>
#include <algorithm>

using namespace std;

int* find_common(int array_1[], int array_2[]){
    int output_array[]={};
    int output_array_count=0;
    for(int i=0; i< sizeof(array_1)/sizeof(int); i++){
        for(int k=0; i< sizeof(array_2)/sizeof(int); k++){
            if(array_1[i]==array_2[k]){
                output_array[output_array_count]=array_1[i];
                output_array_count +=1;
            }
        }
    }
    return output_array;
}

string* find_palindromes(string array_1[]){
    string output_array[]={};
    int output_array_count=0;
    for(int i=0; i< sizeof(array_1)/sizeof(string); i++){
        reverse(array_1[i].begin(),array_1[i].end());
        string temp_string=array_1[i];
        reverse(temp_string.begin(),temp_string.end());
        if(array_1[i].compare(temp_string)==0){
            output_array[output_array_count]=array_1[i];
            output_array_count++;
        }
    }
    return output_array;
}

int main() {

    return 0;
}
