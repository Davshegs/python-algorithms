"""
Problem:
Given a list of emails and URLs, return a dictionary, where each key is the URLs
and the values is how many emails have the same URLs. Note that the URLs begins with www. 
while the email don't have and that email with domain not in the list of URLs should be ignore.

"""

emails = ['foo@a.com', 'bar@a.com', 'baz@b.com', 'quz@d.com']
urls = ['www@a.com', 'www@b.com', 'www@c.com']

emails_domain = [] # creating an empty list where one can store the domain of each email
urls_domain = []   # ctreating and empty list where on can store the domain without the www.

# Using a for loop to extract the domains of each emails and also the domain of each urls without the www.
for i  in emails:
    emails_domain.append(i[-5:])
for j in urls:
    urls_domain.append(j[-5:])

count_urls = {}
# for i in urls_domain:
#     print(i, emails_domain.count(i))

# Using dictionary comprenhension and the count() attribute to extract the number of occurance of each urls domain on the email list  
count_urls = {'www.' + x: emails_domain.count(x) for x in urls_domain }
print(emails_domain)
print(urls_domain)
print(count_urls)