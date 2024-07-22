import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        # linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
        # response = requests.get(
        #     linkedin_profile_url,
        #     # timeout=10,
        # )
        response = {
            "public_identifier": "pratikpatil24",
            "first_name": "pratik",
            "last_name": "patil",
            "full_name": "pratik patil",
            "occupation": "software developer",
            "country": "IN",
            "country_full_name": "india",
            "city": "pune",
            "state": "maharashtra",
            "experiences": [
                {
                    "starts_at": {"day": 1, "month": 7, "year": 2020},
                    "ends_at": None,
                    "company": "cakesoft technologies private limited",
                    "company_linkedin_profile_url": None,
                    "company_facebook_profile_url": None,
                    "title": "software developer",
                    "description": None,
                    "location": None,
                    "logo_url": None,
                },
                {
                    "starts_at": {"day": 1, "month": 9, "year": 2018},
                    "ends_at": {"day": 1, "month": 1, "year": 2020},
                    "company": "pict acm student chapter",
                    "company_linkedin_profile_url": None,
                    "company_facebook_profile_url": None,
                    "title": "chairman",
                    "description": None,
                    "location": None,
                    "logo_url": None,
                },
            ],
            "education": [
                {
                    "starts_at": {"day": 1, "month": 1, "year": 2016},
                    "ends_at": {"day": 1, "month": 1, "year": 2020},
                    "field_of_study": None,
                    "degree_name": "bachelor of engineering,bachelors",
                    "school": "pune institute of computer technology",
                    "school_linkedin_profile_url": "https://www.linkedin.com/company/pict-debsoc",
                    "school_facebook_profile_url": None,
                    "description": None,
                    "logo_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/company/pict-debsoc/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20240722%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20240722T164323Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=45af632f069163a71f711a32d2238e4f5b092c25acff5aa0a2d72ba2347b1017",
                    "grade": None,
                    "activities_and_societies": None,
                }
            ],
            "connections": 500,
        }
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://in.linkedin.com/in/pratikpatil24",
        )
    )
