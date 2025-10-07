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
  ll sum = 0;
  while (n --)
  {
    string s;
    cin >> s;
    if(s == "Tetrahedron")
      sum += 4;
    else if(s == "Cube")
      sum += 6;
    else if(s == "Octahedron")
      sum += 8;
    else if(s == "Dodecahedron")
      sum += 12;
    else if(s == "Icosahedron")
      sum += 20;
  }

  cout << sum << endl;
  return 0;
}