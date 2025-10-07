#include<bits/stdc++.h> 
using namespace std;
#define ll long long
#define loop(i,a,b) for(int i = a; i < b; i++)
#define vll vector<ll>
#define pb push_back
#define endl "\n"

int main()
{
  ll n;
  cin >> n;
  ll count = 0;
  while (n!=0)
  {
    ll rem = n%10;
    if(rem == 7 || rem == 4)
    {
      count++;
    }
    n = n/10;
  }
  if(count == 0)
  {
    cout << "NO" << endl;
    return 0;
  }

  while (count!= 0)
  {
    ll rem = count%10;
    if(rem != 7 && rem != 4)
    {
      cout << "NO" << endl;
      return 0;
    }
    count = count/10;
  }
  cout <<"YES" << endl;
  
  return 0;
}