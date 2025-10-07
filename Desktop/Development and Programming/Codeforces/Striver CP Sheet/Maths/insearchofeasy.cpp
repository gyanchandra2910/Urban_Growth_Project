#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define all(x) x.begin(),x.end()
#define loop(i,a,b) for(int i=a;i<b;i++)
#define rloop(i,a,b) for(int i=a-1;i>=b;i--)

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  ll n;
  cin >> n;
  vector<ll> a(n);
  loop(i,0,n)
    cin >> a[i];
  
  bool checkHardOrEasy = true;
  loop(i,0,n)
  {
    if(a[i] == 1)
    {
      checkHardOrEasy = false;
      break;
    }
  }
  if(checkHardOrEasy)
    cout << "EASY" << endl;
  else
    cout << "HARD" << endl;
  return 0;
}