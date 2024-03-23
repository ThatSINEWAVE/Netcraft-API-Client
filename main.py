import requests
import json
import os


def report_single_url(email, message, url):
    payload = {
        "email": email,
        "urls": [
            {"url": url}
        ]
    }
    if message:
        payload["reason"] = message

    response = requests.post("https://report.netcraft.com/api/v3/report/urls", json=payload)
    if response.status_code == 200:
        uuid = response.json()["uuid"]
        print("[NETCRAFT] Successfully reported:", response.json()["message"])
        print("[NETCRAFT] Submission UUID:", uuid)
        print("[NETCRAFT] Submission Link:", f"https://report.netcraft.com/submission/{uuid}")
    else:
        print("Error reporting URL:", response.text)


def report_urls_from_file(email, message, file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    payload = {
        "email": email,
        "urls": [{"url": url} for url in urls]
    }
    if message:
        payload["reason"] = message

    response = requests.post("https://report.netcraft.com/api/v3/report/urls", json=payload)
    if response.status_code == 200:
        uuid = response.json()["uuid"]
        print("[NETCRAFT] Successfully reported:", response.json()["message"])
        print("[NETCRAFT] Submission UUID:", uuid)
        print("[NETCRAFT] Submission Link:", f"https://report.netcraft.com/submission/{uuid}")
    else:
        print("Error reporting URLs:", response.text)


def report_malicious_mail(email, message, mail_content, password=None):
    payload = {
        "email": email,
        "message": mail_content
    }
    if password:
        payload["password"] = password

    response = requests.post("https://report.netcraft.com/api/v3/report/mail", json=payload)
    if response.status_code == 200:
        uuid = response.json()["uuid"]
        print("[NETCRAFT] Successfully reported:", response.json()["message"])
        print("[NETCRAFT] Submission UUID:", uuid)
        print("[NETCRAFT] Submission Link:", f"https://report.netcraft.com/submission/{uuid}")
    else:
        print("Error reporting mail:", response.text)


def report_incorrectly_blocked_url(email, url, reason):
    payload = {
        "email": email,
        "reason": reason,
        "url": url
    }

    response = requests.post("https://report.netcraft.com/api/v3/report/mistake", json=payload)
    if response.status_code == 200:
        print("[NETCRAFT] Successfully reported incorrectly blocked URL.")
    else:
        print("Error reporting incorrectly blocked URL:", response.text)


def get_submission_details(uuid):
    response = requests.get(f"https://report.netcraft.com/api/v3/submission/{uuid}")
    if response.status_code == 200:
        save_response_to_file(response.json(), f"submission_{uuid}.json")
        print(f"[NETCRAFT] Submission details saved to submission_{uuid}.json")
    else:
        print("Error getting submission details:", response.text)


def get_submission_files(uuid):
    response = requests.get(f"https://report.netcraft.com/api/v3/submission/{uuid}/files")
    if response.status_code == 200:
        submission_dir = f"Submissions/Submission_{uuid}"
        os.makedirs(submission_dir, exist_ok=True)
        for file_data in response.json()["files"]:
            file_hash = file_data["hash"]
            file_name = file_data["filename"]
            file_response = requests.get(f"https://report.netcraft.com/api/v3/submission/{uuid}/files/{file_hash}/content")
            if file_response.status_code == 200:
                file_path = os.path.join(submission_dir, file_name)
                with open(file_path, "wb") as f:
                    f.write(file_response.content)
                print(f"[NETCRAFT] File '{file_name}' saved to {submission_dir}")
            else:
                print(f"Error getting file '{file_name}': {file_response.text}")
    else:
        print("Error getting submission files:", response.text)


def save_response_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def get_submission_urls(uuid):
    response = requests.get(f"https://report.netcraft.com/api/v3/submission/{uuid}/urls")
    if response.status_code == 200:
        save_response_to_file(response.json(), f"submission_{uuid}.json")
        print(f"[NETCRAFT] Submission URLs saved to submission_{uuid}.json")
    else:
        print("Error getting submission URLs:", response.text)


def report_submission_issue(uuid, file_misclassifications, url_misclassifications, additional_info):
    payload = {
        "additional_info": additional_info,
        "filename_misclassifications": file_misclassifications,
        "url_misclassifications": url_misclassifications
    }

    response = requests.post(f"https://report.netcraft.com/api/v3/submission/{uuid}/report_issue", json=payload)
    if response.status_code == 200:
        print("[NETCRAFT] Successfully reported issue with submission.")
    else:
        print("Error reporting issue with submission:", response.text)


def get_available_tags(tag_type):
    response = requests.get(f"https://report.netcraft.com/api/v3/tags/{tag_type}")
    if response.status_code == 200:
        print(f"[NETCRAFT] Available {tag_type} tags:")
        print(response.json())
    else:
        print(f"Error getting available {tag_type} tags:", response.text)


def unsubscribe_from_notifications(email, csrf_token):
    params = {
        "email": email,
        "csrf_token": csrf_token
    }

    response = requests.post("https://report.netcraft.com/api/v3/submitter/unsubscribe", params=params)
    if response.status_code == 200:
        print("[NETCRAFT] Successfully unsubscribed from notifications.")
    else:
        print("Error unsubscribing from notifications:", response.text)


def display_menu():
    print("Netcraft API Commands:")
    print("1. Report a single URL")
    print("2. Report URLs from a file")
    print("3. Report a malicious mail")
    print("4. Report an incorrectly blocked URL")
    print("5. Get submission details")
    print("6. Get submission files")
    print("7. Get submission URLs")
    print("8. Report an issue with a submission")
    print("9. Get available tags")
    print("10. Unsubscribe from notifications")
    print("0. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter your email address: ")
            message = input("Enter a message for the report (optional): ")
            url = input("Enter the URL: ")
            report_single_url(email, message, url)

        elif choice == "2":
            email = input("Enter your email address: ")
            message = input("Enter a message for the report (optional): ")
            file_path = input("Enter the file path: ")
            report_urls_from_file(email, message, file_path)

        elif choice == "3":
            email = input("Enter your email address: ")
            message = input("Enter a message for the report (optional): ")
            mail_content = input("Enter the mail content in MIME format: ")
            password = input("Enter the password for decryption (if applicable): ") or None
            report_malicious_mail(email, message, mail_content, password)

        elif choice == "4":
            email = input("Enter your email address: ")
            url = input("Enter the URL: ")
            reason = input("Enter the reason for reporting: ")
            report_incorrectly_blocked_url(email, url, reason)

        elif choice == "5":
            uuid = input("Enter the submission UUID: ")
            get_submission_details(uuid)

        elif choice == "6":
            uuid = input("Enter the submission UUID: ")
            get_submission_files(uuid)

        elif choice == "7":
            uuid = input("Enter the submission UUID: ")
            get_submission_urls(uuid)

        elif choice == "8":
            uuid = input("Enter the submission UUID: ")
            file_misclassifications = input("Enter misclassified file names (separated by commas): ").split(",")
            url_misclassifications = input("Enter misclassified URLs (separated by commas): ").split(",")
            additional_info = input("Enter additional information: ")
            report_submission_issue(uuid, file_misclassifications, url_misclassifications, additional_info)

        elif choice == "9":
            tag_type = input("Enter the tag type (file, mail, or url): ")
            get_available_tags(tag_type)

        elif choice == "10":
            email = input("Enter your email address: ")
            csrf_token = input("Enter the CSRF token: ")
            unsubscribe_from_notifications(email, csrf_token)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()  # Print an empty line for better readability


if __name__ == "__main__":
    main()
