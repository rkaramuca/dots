#include <iostream>
using namespace std;

int nthUglyNumber(int n);

int main()
{
	int n = 10;
	int ans = nthUglyNumber(n);
	cout << "Ans: " << ans << endl;
	return 0;
}

int nthUglyNumber(int n)
{
	int ugly[n];
	int i2 = 0, i3 = 0, i5 = 0;
	int next_multiple_of_2 = 2;
	int next_multiple_of_3 = 3;
	int next_multiple_of_5 = 5;
	int next_ugly_no = 1;

	ugly[0] = 1;
	for( int i = 1; i < n; i++ )
	{
		next_ugly_no = min(next_multiple_of_2, 
                           min(next_multiple_of_3, 
                               next_multiple_of_5)); 
       		ugly[i] = next_ugly_no; 
       		if (next_ugly_no == next_multiple_of_2) 
       		{ 
           		i2 = i2+1; 
           		next_multiple_of_2 = ugly[i2]*2; 
       		} 
       		if (next_ugly_no == next_multiple_of_3) 
       		{	 
           		i3 = i3+1; 
           		next_multiple_of_3 = ugly[i3]*3; 
       		}	 
       		if (next_ugly_no == next_multiple_of_5) 
       		{ 
           		i5 = i5+1; 
           		next_multiple_of_5 = ugly[i5]*5; 
       		} 
    	}	 /*End of for loop (i=1; i<n; i++) */
    	return next_ugly_no; 
}
