#include<iostream>
#include <fstream>
int main()
{
	int n;
	std::cin>>n;
	double a[n][n+1];
	for(int i = 0; i<n; i++)
		for(int j = 0; j<n; j++)
			std::cin>>a[i][j];
	std::fstream output;
	output.open("F:\\ppt\\chapter3\\input.txt" );
	output<<n<<"\n";
	for(int i = 0; i<n; i++)
		for(int j = 0; j<n; j++)
			output<<a[i][j]<<"\n";
	output.close();
}
