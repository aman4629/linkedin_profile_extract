# create python virtual environment 
# by running -> python -m venv env
           # -> source env/bin/activate
# please install linkedin_api via pip first 
#->  pip install linkedin_api


from linkedin_api import Linkedin

api = Linkedin('example@gmail.com', 'example') #Enter your linkedin email and password

profiles = ["williamhgates"]  # list for linkedin profiles to be extracted

for profile in profiles:
    try:
        profile_data = api.get_profile(profile)
        print(f"Profile data for {profile}:")
        print(profile_data)
        print("\n")
    except Exception as e:
        print(f"error while fetching profile {profile}: {e}")

