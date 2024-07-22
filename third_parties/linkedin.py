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
            "public_identifier": "eden-marco",
            "profile_pic_url": "https://storage.cloud.google.com/publick-profile-pics/1610187870291.jpeg",
            "background_cover_image_url": None,
            "first_name": "Eden",
            "last_name": "Marco",
            "full_name": "Eden Marco",
            "follower_count": None,
            "occupation": "Customer Engineer at Google",
            "headline": "Customer Engineer @ Google Cloud | Best-selling Udemy Instructor",
            "summary": "Backend developer, Udemy.com best seller instructor\\n",
            "country": "IL",
            "country_full_name": "Israel",
            "city": None,
            "state": None,
            "experiences": [
                {
                    "starts_at": {"day": 1, "month": 6, "year": 2022},
                    "ends_at": None,
                    "company": "Google",
                    "company_linkedin_profile_url": "https://www.linkedin.com/company/google/",
                    "title": "Customer Engineer",
                    "description": None,
                    "location": "Tel Aviv, Israel",
                    "logo_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/company/google/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230513%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230513T080203Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=229dbe9195af817a98adea2dcb15487bdb174bef937c40285127f28db5670793",
                },
                {
                    "starts_at": {"day": 1, "month": 4, "year": 2020},
                    "ends_at": {"day": 1, "month": 6, "year": 2022},
                    "company": "Orca Security",
                    "company_linkedin_profile_url": "https://www.linkedin.com/company/orca-security/",
                    "title": "Software Engineer",
                    "description": None,
                    "location": "Tel Aviv, Israel",
                    "logo_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/company/orca-security/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230513%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230513T080203Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=315aa0e922c856498926881eece4c08c003aa5bb059af42346c9391f8cfcd475",
                },
                {
                    "starts_at": {"day": 1, "month": 12, "year": 2019},
                    "ends_at": {"day": 1, "month": 4, "year": 2020},
                    "company": "Wizer",
                    "company_linkedin_profile_url": "https://www.linkedin.com/company/get-wizer/",
                    "title": "Software Engineer",
                    "description": None,
                    "location": None,
                    "logo_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/company/get-wizer/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230513%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230513T080203Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=a39d39ef340f06a1f46f0c48f73516dbf5a3a30a1dbb4a380574255a66ff0f95",
                },
                {
                    "starts_at": {"day": 1, "month": 7, "year": 2019},
                    "ends_at": {"day": 1, "month": 12, "year": 2019},
                    "company": "Deep Instinct",
                    "company_linkedin_profile_url": "https://www.linkedin.com/company/deep-instinct/",
                    "title": "Software Engineer",
                    "description": None,
                    "location": "Tel Aviv Area, Israel",
                    "logo_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/company/deep-instinct/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230513%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230513T080203Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=ac30ed0fedb0b001da7dc600eca6893590dd26c4b4bac5865c5887ef7491189f",
                },
                {
                    "starts_at": {"day": 1, "month": 10, "year": 2018},
                    "ends_at": {"day": 1, "month": 7, "year": 2019},
                    "company": "Reichman University (IDC Herzliya)",
                    "company_linkedin_profile_url": "https://www.linkedin.com/school/reichman-university/",
                    "title": "Computer Science Teaching Assistant (External Lecturer)",
                    "description": "* Functional Programming (Including international school)\\n* Introduction to Computer Science",
                    "location": "Herzliya Area, Israel",
                    "logo_url": "https://media.licdn.com/dms/image/C4D0BAQGg9wJflAQnjw/company-logo_400_400/0/1632054179547?e=1690416000&v=beta&t=wnKrHMYOoMiR6yV4-C8oMXhWEHmS20QRVR6Qat8WrTA",
                },
                {
                    "starts_at": {"day": 1, "month": 2, "year": 2017},
                    "ends_at": None,
                    "company": "Udemy",
                    "company_linkedin_profile_url": "https://www.linkedin.com/company/udemy/",
                    "title": "Independent Udemy Instructor",
                    "description": "Production and publication of two best-selling courses on the Udemy platform, with a total of 9k+ enrolled students, 800+ ratings and a solid 4.7 \\u2605 rating.",
                    "location": None,
                    "logo_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/company/udemy/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230513%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230513T080203Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=caf871d9951df0d29e82a02f432ad6b5c2bd71c2dbf0db08224e3fa5c51ee1db",
                },
                {
                    "starts_at": {"day": 1, "month": 7, "year": 2010},
                    "ends_at": {"day": 1, "month": 8, "year": 2014},
                    "company": "Israel Defense Forces",
                    "company_linkedin_profile_url": "https://www.linkedin.com/company/israeldefenseforces/",
                    "title": "Captain",
                    "description": None,
                    "location": None,
                    "logo_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/company/israeldefenseforces/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230513%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230513T080203Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=adf57f88519d84d6f9f2d4e887185fb1c50d698462e51d4c8c7907779a4fe16f",
                },
            ],
            "education": [
                {
                    "starts_at": {"day": 1, "month": 1, "year": 2015},
                    "ends_at": {"day": 1, "month": 1, "year": 2019},
                    "field_of_study": "Computer Science",
                    "degree_name": "Bachelor\\u2019s Degree",
                    "school": "Technion - Israel Institute of Technology",
                    "school_linkedin_profile_url": None,
                    "description": None,
                    "logo_url": "https://media.licdn.com/dms/image/C4D0BAQG12formuFdJg/company-logo_400_400/0/1559649766994?e=1690416000&v=beta&t=0_rUTMww9U95TDh7RBjiFXp2G-k3hGMSpgt7d2XaRo8",
                    "grade": None,
                    "activities_and_societies": None,
                }
            ],
            "languages": [],
            "accomplishment_organisations": [],
            "accomplishment_publications": [],
            "accomplishment_honors_awards": [],
            "accomplishment_patents": [],
            "accomplishment_courses": [],
            "accomplishment_projects": [],
            "accomplishment_test_scores": [],
            "volunteer_work": [],
            "certifications": [],
            "connections": None,
            "people_also_viewed": [],
            "recommendations": [],
            "activities": [],
            "similarly_named_profiles": [
                {
                    "name": "Blumeden Marco Pasquali",
                    "link": "https://it.linkedin.com/in/blumeden-marco-pasquali-44603287",
                    "summary": "--",
                    "location": "Italy",
                },
                {
                    "name": "Eden Marco",
                    "link": "https://www.linkedin.com/in/edenmarco",
                    "summary": "Incoming Deloitte Strategy Summer Scholar",
                    "location": "Chapel Hill, NC",
                },
                {
                    "name": "Eden Marco",
                    "link": "https://www.linkedin.com/in/eden-marco-8299301ba",
                    "summary": "Student at San Francisco State University",
                    "location": "San Francisco Bay Area",
                },
                {
                    "name": "Eden Marco",
                    "link": "https://www.linkedin.com/in/eden-marco-875211201",
                    "summary": "Incoming First Year Optometry Student at Massachusetts College of Pharmacy & Health Sciences",
                    "location": "Greater Boston",
                },
            ],
            "articles": [],
            "groups": [],
            "phone_numbers": [],
            "social_networking_services": [],
            "skills": [],
            "inferred_salary": None,
            "gender": None,
            "birth_date": None,
            "industry": None,
            "extra": None,
            "interests": [],
            "personal_emails": [],
            "personal_numbers": [],
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

    # data = response.json()
    # data = {
    #     k: v
    #     for k, v in data.items()
    #     if v not in ([], "", "", None)
    #     and k not in ["people_also_viewed", "certifications"]
    # }
    # if data.get("groups"):
    #     for group_dict in data.get("groups"):
    #         group_dict.pop("profile_pic_url")
    # return data

    return response


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
        )
    )
