#include<bits/stdc++.h>
using namespace std;
int noOfDigits(int n)
{
  int cnt = 0;
  while(n > 0)
  {
    n /= 10;
    cnt++;
  }
  return cnt;
}

int main()
{
  int n;
  cin >> n;
  int noOfDigitsInN = noOfDigits(n);
  int ans = 0, cnt = 1;
  while (n != 0)
  {
    int rem = n % 10;
    int newNo;
    if(noOfDigitsInN != 0)
    {
      if(rem > 4)
      {
        newNo = 9 - rem;
      }
    }
    else
    {
      newNo = rem;
    }

    ans = cnt * newNo + ans;
    cnt *= 10;
    n /= 10;
    noOfDigitsInN--;
  }
  
  cout << ans << endl;

  return 0;
}