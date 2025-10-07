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
  
  ll minimum_val = *min_element(all(a));
  ll min_index = min_element(all(a)) - a.begin();
  ll maximum_val = *max_element(all(a));
  ll max_index = max_element(all(a)) - a.begin();
  ll ans = 0;

  for(ll i = 0; i < n; i++)
  {
    if(a[i] == minimum_val)
    {
      min_index = i;
    }
  }

  // cout << min_index << " " << max_index << endl;
  if(max_index < min_index)
  {
    ans += n - min_index - 1;
    ans += max_index;
  }
  else
  {
    ans += max_index;
    ans += n - min_index - 2;
  }
  cout << ans << endl;
  return 0;
}