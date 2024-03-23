# Netcraft API Client

This Python script provides a command-line interface for interacting with the Netcraft API. It allows users to perform various actions such as reporting malicious URLs, malicious emails, and incorrectly blocked URLs, as well as retrieving details about submitted reports.

## Features

- Report a single URL
- Report multiple URLs from a file
- Report a malicious email (with optional password for decryption)
- Report an incorrectly blocked URL
- Get details of a submitted report
- Download files associated with a submitted report
- Get URLs associated with a submitted report
- Report an issue with a submitted report (e.g., file or URL misclassifications)
- Get available tags for file, mail, or URL reports
- Unsubscribe from notification emails

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Usage

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the script using `python main.py`.
4. Follow the prompts in the command-line interface to perform the desired actions.

Example usage:
Then, follow the menu options and provide the required inputs.

## Function Documentation

### `report_single_url(email, message, url)`

Reports a single URL to the Netcraft API.

- `email`: The email address of the submitter.
- `message`: An optional message to include with the report.
- `url`: The URL to be reported.

### `report_urls_from_file(email, message, file_path)`

Reports multiple URLs from a file to the Netcraft API.

- `email`: The email address of the submitter.
- `message`: An optional message to include with the report.
- `file_path`: The path to the file containing the URLs (one URL per line).

### `report_malicious_mail(email, message, mail_content, password=None)`

Reports a malicious email to the Netcraft API.

- `email`: The email address of the submitter.
- `message`: An optional message to include with the report.
- `mail_content`: The content of the malicious email in MIME format.
- `password`: An optional password for decrypting the email (if applicable).

### `report_incorrectly_blocked_url(email, url, reason)`

Reports an incorrectly blocked URL to the Netcraft API.

- `email`: The email address of the submitter.
- `url`: The URL that was incorrectly blocked.
- `reason`: The reason for reporting the incorrectly blocked URL.

### `get_submission_details(uuid)`

Retrieves the details of a submitted report and saves them to a JSON file.

- `uuid`: The UUID of the submitted report.

### `get_submission_files(uuid)`

Downloads the files associated with a submitted report.

- `uuid`: The UUID of the submitted report.

### `get_submission_urls(uuid)`

Retrieves the URLs associated with a submitted report and saves them to a JSON file.

- `uuid`: The UUID of the submitted report.

### `report_submission_issue(uuid, file_misclassifications, url_misclassifications, additional_info)`

Reports an issue with a submitted report, such as file or URL misclassifications.

- `uuid`: The UUID of the submitted report.
- `file_misclassifications`: A list of misclassified file names.
- `url_misclassifications`: A list of misclassified URLs.
- `additional_info`: Additional information about the issue.

### `get_available_tags(tag_type)`

Retrieves the available tags for file, mail, or URL reports.

- `tag_type`: The type of tags to retrieve ('file', 'mail', or 'url').

### `unsubscribe_from_notifications(email, csrf_token)`

Unsubscribes the provided email address from notification emails.

- `email`: The email address to unsubscribe.
- `csrf_token`: The CSRF token required for unsubscribing.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
