
// SQRT Decomposition
#include <bits/stdc++.h>
using namespace std;

#define MAXN 10000
#define SQRSIZE 100

int arr[MAXN];      // original array
int block[SQRSIZE]; // decomposed(in block of sqrt size) array
int blk_sz;         // block size

// Building block array or preprocessing input array and filling block array
void Build(int input[], int n)
{
    int blk_idx = -1;

    blk_sz = sqrt(n);

    for (int i = 0; i < n; i++)
    {
        arr[i] = input[i];

        if (i % blk_sz == 0)
            blk_idx++;

        block[blk_idx] += arr[i];
    }
}

// Point Update
void Update(int index, int value)
{
    int block_number = index / blk_sz;
    block[block_number] += (value - arr[index]);
    arr[index] = value;
}

// Quering the preprocessed array or block array
int Query(int l, int r)
{
    int sum = 0;

    while (l < r && l % blk_sz != 0 && l != 0)
    {
        sum += arr[l];
        l++;
    }

    while (l + blk_sz <= r)
    {
        sum += block[l / blk_sz];
        l += blk_sz;
    }

    while (l <= r)
    {
        sum += arr[l];
        l++;
    }

    return sum;
}

int main()
{
    int input[] = {1, 5, 2, 4, 6, 1, 3, 5, 7, 10};
    int n = sizeof(input) / sizeof(input[0]);

    Build(input, n);

    cout << "query(3,8) : " << Query(3, 8) << endl;
    cout << "query(1,6) : " << Query(1, 6) << endl;

    Update(8, 0);

    cout << "query(8,8) : " << Query(8, 8) << endl;

    return 0;
}
