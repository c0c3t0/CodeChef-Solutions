## Problem
You are given two strings S and A of lengths N and M respectively.
- String S contains characters from the set {?, a, b, c, d, e}.
- String A contains characters from the set {a, b, c, d, e}.

Let S<sup>′</sup> denote the string formed by replacing all the ? in S using the characters from the set {a, b, c, d, e}.
Construct S<sup>′</sup> such that A is not a subsequence of S<sup>′</sup>.

If multiple such S<sup>′</sup> exist, output any. If no such S<sup>′</sup> exists, print −1.

### Input Format
- The first line will contain T - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers N and M - the lengths of strings S and A respectively.
- The second line of each test case contains string S.
- The third line of each test case contains string A.

### Output Format
For each test case, output any valid string S<sup>′</sup>. If no such string exists, print −1.

### Sample 1:
<pre><code>Input:
2
4 2
?ab?
ba
4 2
a??b
ab
</code></pre>
<pre><code>
Output:
aabe
-1
</code></pre>
