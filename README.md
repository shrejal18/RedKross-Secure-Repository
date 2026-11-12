# RedKross – Secure Repository Starter

## 1. Project Overview

This project demonstrates a reusable secure repository starter with automated CI security checks.

It uses a fictional Flask training service to demonstrate secure software development practices, automated testing, dependency auditing, secret scanning and Software Bill of Materials (SBOM) validation.

This is a defensive training project and is not intended for production deployment.

## 2. Objectives

- Implement input validation and error handling.
- Create automated application tests.
- Identify common Python security issues.
- Audit dependencies for known vulnerabilities.
- Detect common secret patterns in repository files.
- Validate SBOM components against the dependency manifest.
- Automate security checks using GitHub Actions.

## 3. Technologies Used

- Python 3.13
- Flask
- Pytest
- Bandit
- pip-audit
- Git and GitHub
- GitHub Actions
- CycloneDX SBOM format
- JSON

## 4. Project Structure

```text
secure-service/
│
├── .github/
│   └── security-checks.yml
│
├── scripts/
│   ├── secret_scan.py
│   └── validate_sbom.py
│
├── tests/
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── package.json
├── sbom_fixture.json
├── advisory_fixture.json
├── .env.example
├── .gitignore
├── SECURITY_REVIEW.md
└── README.md
```

## 5. Installation

Clone the repository:

```bash
git clone https://github.com/shrejal18/RedKross-Secure-Repository.git
```

Move into the project directory:

```bash
cd RedKross-Secure-Repository
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## 6. Running the Application

```bash
python app.py
```

Application endpoints:

- GET /health – Health status.
- POST /profile – Validates profile input.

## 7. Automated Testing

Run:

```bash
python -m pytest -v
```

Six tests cover valid input, invalid input type, oversized input, missing input, empty input and the health endpoint.

## 8. Security Checks

### Bandit – Python Security Scan

```bash
python -m bandit -r app.py
```

### Dependency Audit

```bash
python -m pip_audit -r requirements.txt
```

### Secret Scanning

```bash
python scripts/secret_scan.py
```

### SBOM Validation

```bash
python scripts/validate_sbom.py
```

The SBOM script checks the training SBOM format, required component fields and consistency with package.json. It is not a full official CycloneDX schema validator.

## 9. GitHub Actions

Workflow file:

`.github/security-checks.yml`

The workflow runs automatically on pushes and pull requests.

It performs:

1. Repository checkout.
2. Python environment check.
3. Dependency installation.
4. Automated tests.
5. Bandit security scan.
6. Dependency vulnerability audit.
7. Secret scanning.
8. SBOM validation.

The workflow uses read-only repository permissions.

## 10. Security Practices

- Validate user input.
- Reject unexpected input fields.
- Limit input length.
- Never commit real secrets.
- Use .gitignore to exclude sensitive and temporary files.
- Audit dependencies regularly.
- Automate security checks through CI.

## 11. Testing Results

The following checks were successfully completed:

- Six automated tests passed.
- Bandit reported zero issues.
- pip-audit reported no known vulnerabilities after dependency updates.
- Secret scanner completed successfully.
- SBOM validation passed.
- GitHub Actions workflow completed successfully.

These results reflect the checks performed during this project and do not guarantee complete application security.

## 12. Limitations

- This is a fictional training application.
- The secret scanner uses basic patterns and may miss secrets or produce false positives.
- SBOM validation is a training-level consistency check.
- Advisory fixture entries are synthetic, not genuine CVEs.
- Further security testing is required before real deployment.

## 13. Conclusion

This project demonstrates how secure coding, automated testing, dependency auditing, secret scanning and SBOM validation can be combined through GitHub Actions to support secure software development.

## 14. GitHub Repository

Repository URL:

https://github.com/shrejal18/RedKross-Secure-Repository