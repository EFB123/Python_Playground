import requests
response = requests.get("https://randomuser.me/api/")

def newLines(number):
    for i in range(number):
        print('')


#print(type(response))
#status_code = response.status_code 
#print("Status code is: ", status_code,newLines(10))
#headers = response.headers # represents the headers as a dictionary
#print("Headers is: ", headers, newLines(10))
#text = response.text    # represents the response body as a strings
#print("Body as string is: ", text, newLines(10))
#content = response.content # represents the response body as a binary
#print("Body as binary is: ", content, newLines(10))
#json_format = response.json()  # parses the response body in JSON format
#print("Json format of respose body is: ", json_format, newLines(10))
#request = response.request # represents the request as requests.models.PreparedRequest
#print("Request I sent is: ", request, newLines(10))

#Plocka ut relevanta delar ur requests body för att manipulera på något sätt
#Skapa relevanta klasser och arv som kan uppta den omvandlade informationen
#Test cases; Försök få full code coverage(testen går igenom alla kodrader)
#Skapa någon typ av GUI(((Valbart)))

"""
This is a method to only return what is inside of a paranthesis of the given string.
Method is aware of how deeply nested you are and you can utilize this.
"""
def inside_par(s):
    stack = []
    word = ""
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
        if not len(stack) == 0 and c != '(':
            word += c
    return word


"""
This is a method to make a list of all the quotes within a text
It does not handle nested quotes and will fail if such occurances exist!!!
"""
def quotes_only(s):
    quote_list = [] # List of quotes
    inside_quotation = False
    quote = ""
    for c in s:
        if c == "\"" and not inside_quotation: #look for new qoute
            inside_quotation = True
        elif inside_quotation and not c == "\"":#save char to current qoute
            quote += c
        elif inside_quotation and c == "\"": #exit quotation
            inside_quotation = False
            quote_list.append(quote)
            quote = ""
    return quote_list

#Test the 
print(quotes_only(response.text))