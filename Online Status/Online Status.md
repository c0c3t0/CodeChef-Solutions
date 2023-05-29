## Online Status
The aim of this challange is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

<pre><code>
statuses = {
    'Alice': 'online',
    'Bob': 'offline', 
    'Eve': 'online',
}
</code></pre>

In this case, the number of people online is 2.

Write a function online_count that takes a dictionary as its parameter. The dictionary maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.