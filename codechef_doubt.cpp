// Name  : Shreyas Sanjay Nanaware
// TE EXTC 
// Roll No  : 41

#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t , N , arr[0] , result = 0;
	cin >> t;
	for(int i=0;i<t;i++){
	    cin >> N;
	    for(int z=0;z<N;z++){
	        cin >> arr[z];
	        if(arr[z]<0){
	            result = result + 1;
	        }
	        
	}
	    if(result %2!=0){
	        cout << "1" << endl;
	   }
	    else{
	        cout << "0" << endl;
	   }
	        
	           

}
	return 0;
}
