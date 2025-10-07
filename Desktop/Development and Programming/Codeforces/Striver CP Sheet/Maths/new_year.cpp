#include<bits/stdc++.h> 
using namespace std;
#define ll long long
#define all(x) x.begin(),x.end()

int main()
{
  vector<ll> a(3);
  cin >> a[0] >> a[1] >> a[2];
  sort(all(a));

  ll ans = abs(a[1] - a[0]) + abs(a[2] - a[1]);
  cout << ans << endl;
  return 0;
}