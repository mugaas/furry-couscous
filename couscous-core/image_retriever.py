import requests
from argparse import ArgumentParser
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--image", help="Image URL", required=True)
    parser.add_argument("-d", "--destination", help="Destination Directory")
    args = parser.parse_args()
    current_dir = os.path.dirname(__file__)
    destination_dir = os.path.join(current_dir, 'temp')
    if args.destination:
        destination_dir = os.path.join(args.destination)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    print(args.image)
    print(destination_dir)
    extension(args.image, destination_dir)

def extension(image_url, local_dest):
    if image_url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        getImage(image_url, local_dest)
    else: 
        getScreen(image_url, local_dest)

def getImage(image_url, local_dest):
    # URL of the image to be downloaded is defined as image_url
    r = requests.get(image_url) # create HTTP response object
    
    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    newname = image_url.split('/')[-1]
    full_file_path = os.path.join(local_dest, newname)
    print(full_file_path)
    with open(full_file_path,'wb') as f:
        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)
    return full_file_path

def getScreen(image_url, local_dest):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    #options.binary_location = "$PATH/chromedriver"
    
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(image_url)
    
    newname = ('screenshot.png')
    full_file_path = os.path.join(local_dest, newname)
    
    driver.save_screenshot(full_file_path)
    driver.close()

if __name__ == "__main__":
    main()

    
