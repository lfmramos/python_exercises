"""
Given 'n' names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each 'name' queried, print the associated entry from your phone book on a new line in the form 'name=phoneNumber';
if an entry for 'name' is not found, print 'Not found' instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format
The first line contains an integer, 'n', denoting the number of entries in the phone book.
Each of the 'n' subsequent lines describes an entry in the form of '2' space-separated values on a single line.
The first value is a friend's name, and the second value is an 8-digit phone number.

After the n lines of phone book entries, there are an unknown number of lines of queries.
Each line (query) contains a 'name' to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.

Output Format
On a new line for each query, print 'Not found' if the name has no corresponding entry in the phone book;
otherwise, print the full 'name' and 'phoneNumber' in the format 'name=phoneNumber'.
"""
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read the number of entries in the phone book
    n = int(data[0])
    
    # Initialize the phone book dictionary
    phone_book = {}
    
    # Read the phone book entries
    for i in range(1, n + 1):
        name, phone_number = data[i].split()
        phone_book[name] = phone_number
    
    # Process the queries
    for query in data[n + 1:]:
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")

if __name__ == "__main__":
    main()