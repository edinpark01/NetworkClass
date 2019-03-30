# Client / Server TCP communication programming assignment

Using TCP sockets, you will write a simplified version of a HTTP client and server.  The client program will use the 
HTTP protocol to fetch a file from the server using the HTTP GET method, cache it, and then subsequently use 
conditional GET operations to fetch the file only if it has been modified. 

### Notes:
1. Program must use HTTP natively
2. Client and server program must use command-line arguments
3. Server program must use relative filename (file in current directory), not absolute filename


#### Client Instructions
1. Take in a single command line argument that specifies a web url containing:
    1. hostname     
    2. port
    3. file name to be fetched ( only if it has been modified )
2. If the file is not yet cached, use a HTTP GET operation to fetch the file named in the URL
    1. Print out the contents of the file
    2. Cache the file
3. If the file is cached, use a Conditional GET operation for the file named in the URL
    1. If server indicated the file has not been modified since the last download, print output saying so ( no need to print file contents in this case )
    2. Otherweise, indicate that the file has been modified, and print and cache new contents

#### Server Instructions
1. Read a command-line argument specifying:
    1. IP address 
    2. Port
2. Open a TCP socket and listen for incoming HTTP Get and Conditional GET requests from one or more HTTP Clients at above address and port
3. In the case of a HTTP Get request:
    1. Read the named file and return a HTTP GET response, including the Last-Modfied header field
4. In the case of a HTTP Conditional GET request:
    1. If the file has not been modified since that indicated by If-Modified-Since, return the appropriate Not Modified response ( return code 304 )
    2. Otherwise, return the file contens as in step 2
5. In the case that the named file does not exits, return the appropriate "Not found" error ( return code 404 )
6. The server must ignore all header fields in HTTP Requests it does not understand

## Simplifying Assumptions
* Only GET and Conditional GET requests supported
* Only a subset of header fields need to be supported in HTTP Requests and Responses
* The client and server must ignore all header fields it does not understand. For example, a “real’ web browser will 
send many more header fields in GET requests than those expected to be implemented by the server. The server MUST 
ignore these fields and continue processing as if these fields were not part of the GET request. The server MUST NOT 
report an error in these cases.

## Cache Implementation:
* The cache must be implemented as a file so that it persists across client instantiations 
* The file(s) used to implement the cache must include “cache” in the filename so that it is easy to distinguish e.g “cache.txt”
* The program must work as per the test cases across multiple client instantiations, one per test case.
* The client program must work if the cache file does not exist (in which case, the implication is no files have been cached)
* Note that this means the file may have existed after previous runs of your program, but has since been deleted prior to client restarting


## Test Cases
Enable wireshark during all the following test cases. (One wireshark .pcap is fine for the test cases in this section, 
but the .pcap must show the test cases in this order.) Run the client four times, once for each test case.
1.	Run client when web object not cached (or no cache exists): Using your HTTP client, download the contents of a 
    text-based html  file named filename.html from your HTTP server using the appropriate URL. Example: localhost:12000/filename.html. 
    The client must:
    1.	Print out the contents of the header in the HTTP Request
    2.	Print out the contents of the header in the HTTP Response (should indicate a “200 OK ” Response)
    3.	Print out file contents (you can print “as is”. No formatting is required)
2.	Run client when web object cached, but not modified on server: Using your HTTP Client, send a conditional GET 
    request to your HTTP server. The client must:
    1.	Print out the contents of the header in the HTTP Request
    2.	Print out the contents of the header in the HTTP Response (should indicate a “304 Not Modified” Response)
3.	Run client when web object cached, but modified on server: Using your HTTP Client, send a conditional GET request 
    to your HTTP server. The client must:
    1.	Print out the contents of the header in the HTTP Request
    2.	Print out the contents of the header in the HTTP Response.
    3.	Display the new file contents
4.	Web object does not exist: Using your HTTP Client, send a GET request for a filename that does not exist. 
    The client must:
    a.	Print out the contents of the header in the HTTP Request
    b.	Print out the contents of the header in the HTTP Response

#### Test Cases for extra credit:

Using a web browser, such as Firefox or Chrome (note: Safari web browser may not implement the conditional GET as expected), 
perform the same test cases as above on your server. Enable wireshark during all the following test cases. 
One wireshark .pcap is fine for the web browser test cases.
1.	Enter the URL in the web browser search bar and press <return>. The web browser should print the contents of the 
    file downloaded from your server.
2.	Re-enter the URL in the web browser search bar and press <return>. The web browser should show the same web page 
    contents as in step 1 (assuming the file has not been modified.), and the wireshark trace should show a Conditional 
    Get and a “Not Modified” response.
3.	Modify the file. Re-enter the URL in the web browser search bar and press <return>. The web browser should now 
    show the updated web contents.
4.	Enter a non-existent URL, and browser should indicate “Not found”
