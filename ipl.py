import subprocess

# Define the required packages
required_packages = ["requests", "shutil"]

# Install the required packages if they are not already installed
for pkg in required_packages:
    try:
        __import__(pkg)
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.call(["pip", "install", pkg])

# Now import the required modules
import requests
import time
import shutil

# The rest of your code goes here...


def get_geolocation(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return data
            else:
                print("Error:", data['message'])
                return None
        else:
            print("Error: Unable to retrieve geolocation data.")
            return None
    except requests.RequestException as e:
        print("Error:", e)
        return None

def generate_map_link(latitude, longitude):
    return f'https://www.google.com/maps?q={latitude},{longitude}'

def print_separator():
    print("—" * shutil.get_terminal_size().columns)

def main():
    # ASCII art
    print("""
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░   ░▒▓█▓▒░  ░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                                
                                      🔰 𝖨𝖯 𝖫𝗈𝖼𝖺𝗍𝗂𝗈𝗇 𝖳𝗋𝖺𝖼𝗄𝖾𝗋 𝗐𝗂𝗍𝗁 𝖦𝗈𝗈𝗀𝗅𝖾 𝖬𝖺𝗉 𝖫𝗂𝗇𝗄 🔰                                                                                                         

    """)

    # Display notice for 5 seconds
    notice = "Just Copy the victim's IP , Paste here, and Press Enter✌"
    print(notice.center(shutil.get_terminal_size().columns))
    time.sleep(1)

    ip_address = input("Enter the IP address to track: ")
    geolocation_data = get_geolocation(ip_address)
    if geolocation_data:
        print("IP Address:", geolocation_data['query'])
        print_separator()
        print("Country:", geolocation_data['country'])
        print_separator()
        print("City:", geolocation_data['city'])
        print_separator()
        print("ZIP Code:", geolocation_data['zip'])
        print_separator()
        latitude = geolocation_data['lat']
        longitude = geolocation_data['lon']
        map_link = generate_map_link(latitude, longitude)
        print("Google Maps Link:", map_link)
    else:
        print("Unable to retrieve geolocation data.")

if __name__ == "__main__":
    main()
