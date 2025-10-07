#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define all(x) x.begin(),x.end()
#define loop(i,a,b) for(int i=a;i<b;i++)
#define rloop(i,a,b) for(int i=a-1;i>=b;i--)

int main()
{
  ll n, m;
  cin >> n >> m;
  bool right = true;
  loop(r,0,n)
  {
    loop(c,0,m)
    {
      if(r % 2 == 0)
      {
        cout << "#";
      }
      else if (r % 2 == 1)
      {
        if (right && c == m - 1)
        {
          cout << "#";
        }
        else if (!right && c == 0)
        {
          cout << "#";
        }
        else
        {
          cout << ".";
        }
      }
    }
    if (r % 2 == 1)
      right = !right;
    cout << "\n";
  }
  return 0;
}