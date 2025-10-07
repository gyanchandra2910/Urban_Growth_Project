#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define all(x) x.begin(),x.end()
#define loop(i,a,b) for(int i=a;i<b;i++)

void solve()
{
  ll n;
  cin >> n;
  vector<ll> ans;
  ll i = 1, count = 0;
  while (n!=0)
  {
    ll rem = n % 10;
    if (rem != 0)
    {
      ans.push_back(rem * i);
      count++;
    }
    i *= 10;
    n /= 10;
  }
  cout << count << "\n";
  for (auto x : ans)
    cout << x << " ";
  cout << "\n";
  
}

int main()
{
  ll t;
  cin >> t;
  while (t--)
  {
    solve();
  }
  
}