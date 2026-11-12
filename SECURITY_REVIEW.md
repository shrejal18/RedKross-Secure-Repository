# Security Review – RedKross Training Service

## 1. Input Validation

The application validates user input received through the `/profile` endpoint.

Security checks include:
- Only JSON requests are accepted.
- Input must be a valid JSON object.
- The `display_name` field is mandatory.
- The display name must be a string.
- Empty names are rejected.
- Display names cannot exceed 80 characters.
- Unexpected fields are rejected.

## 2. Error Handling

The application returns appropriate HTTP status codes:
- 200 – Request successful.
- 400 – Invalid or missing input.
- 415 – Unsupported content type.

Error messages are returned in JSON format.

## 3. Tests Performed

Six automated tests were created and executed:

1. Health endpoint test.
2. Valid profile input test.
3. Invalid input type test.
4. Oversized display name test.
5. Missing display name test.
6. Empty display name test.

Test result: All 6 tests passed.

## 4. Secret Management

The `.env.example` file contains dummy training values only.

Real API keys, passwords and database credentials must never be committed to GitHub.

The `.gitignore` file excludes `.env` and other temporary files while allowing `.env.example` to remain in the repository.

## 5. Controls Required Before Real Deployment

Before using this application in a real environment, the following controls are required:

- Use HTTPS for secure communication.
- Use proper authentication and authorization.
- Store secrets in a secure secret manager.
- Use a production-ready WSGI server instead of Flask's development server.
- Keep dependencies updated and scan them for known vulnerabilities.
- Add security logging and monitoring.
- Configure rate limiting.
- Review database access and permissions.
- Perform security testing before deployment.

## 6. Dependency and Advisory Review

The supplied `package.json`, SBOM and advisory fixture contain fictional training package names.

The advisory entries are synthetic examples used for practice. They must not be reported as genuine CVEs or real vulnerabilities.

## 7. Limitations

This is a training application, not a production-ready service.

Passing the six tests does not guarantee that the application is completely secure. Further security reviews and testing are required before real deployment.