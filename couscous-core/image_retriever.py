import requests
from argparse import ArgumentParser
import os

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
    getImage(args.image, destination_dir)

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

if __name__ == "__main__":
    main()