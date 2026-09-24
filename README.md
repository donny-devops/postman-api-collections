# Postman API Collections

A curated set of **Postman collections and environments** used to explore, test, and document APIs across projects.

## Overview

This repository contains reusable Postman artefacts for REST (and optionally GraphQL) APIs, including:

- Collections grouped by service or domain
- Preconfigured environments per stage (local, dev, staging, production)
- Example requests and responses
- Test scripts and workflows for regression and smoke testing

You can import these collections into Postman to quickly bootstrap API development, manual testing, and automated checks.[web:34][web:41]

## Repository Structure

```bash
postman-api-collections/
├── README.md
├── collections/
│   ├── api-doc-demo-portal/
│   │   └── api-doc-demo-portal.postman_collection.json
│   ├── security-api-audit/
│   │   └── secops-api-audit.postman_collection.json
│   └── tech-support-agent/
│       └── ai-tech-support-agent.postman_collection.json
├── environments/
│   ├── api-doc-demo-portal-sandbox.postman_environment.example.json
│   ├── secops-sandbox.postman_environment.example.json
│   └── tech-support-agent.postman_environment.example.json
└── scripts/
    └── run_newman_tests.py
```

## Getting Started

### Import into Postman

1. Open Postman (Desktop or Web).
2. Click **Import**.
3. Drag-and-drop or select the `.postman_collection.json` and `.postman_environment.json` files from this repo.
4. Choose the environment (e.g., `local`, `dev`) in the top-right environment selector.

Postman will load all requests, folder structures, and any descriptions defined in the collections.[web:34]

### Environment Variables

Environments are used to store values such as base URLs, API keys, and user credentials so the same collection can target multiple stages.[web:41][web:44]

Typical environment variables:

- `base_url`
- `api_key` or `authorization_token`
- `username` / `password` for test accounts
- `tenant_id`, `org_id`, or similar scoping identifiers

Example variable usage in requests:

```http
GET {{base_url}}/v1/users/{{user_id}}
Authorization: Bearer {{authorization_token}}
```

Update the environment JSON files or Postman environment editor with values appropriate for your setup.

## Collection Conventions

To keep collections consistent and easy to navigate, follow these conventions:[web:37][web:40][web:46]

- Folder structure: group requests by feature or resource (e.g., `Auth`, `Users`, `Orders`).
- Naming: prefix request names with HTTP method (e.g., `GET List Users`, `POST Create User`).
- Documentation: add descriptive text for each request and folder explaining purpose, auth requirements, and expected responses.
- Examples: attach success and error examples (200, 400, 401, 404, 500) where useful.[web:34]
- Pre-request scripts: use to set auth headers, generate dynamic values, or chain data from previous requests.
- Tests: add basic assertions for status codes, schema, and key fields to support regression.[web:42]

### Validate Schema & Collections
You can validate the JSON schema and structure of all collections and environments:

```bash
python scripts/run_newman_tests.py
```

### Quick Start with npm Scripts

If you have Node.js installed, you can run tests and generate reports using `npm`:

```bash
# Validate schemas
npm test

# Run individual collections with Newman
npm run test:secops
npm run test:demo-portal
npm run test:support-agent

# Run all collections sequentially
npm run test:all

# Generate HTML Extra visual reports
npm run report:secops
npm run report:all
```

### Running Collections with Newman

You can run these collections in CI/CD or locally using **Newman**, Postman’s CLI runner.

#### Install Newman

```bash
npm install -g newman newman-reporter-htmlextra
```

#### Run SecOps Audit Suite

```bash
newman run collections/security-api-audit/secops-api-audit.postman_collection.json \
  -e environments/secops-sandbox.postman_environment.example.json
```

#### Generate Rich HTML Extra Report

```bash
newman run collections/security-api-audit/secops-api-audit.postman_collection.json \
  -e environments/secops-sandbox.postman_environment.example.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export reports/secops-audit-report.html
```

### Continuous Integration (GitHub Actions)

The [.github/workflows/newman-ci.yml](.github/workflows/newman-ci.yml) workflow runs on push and pull requests to `main`:
1. **Schema Validation**: Runs `scripts/run_newman_tests.py` to validate collection and environment schemas.
2. **Matrix Test Execution**: Executes Newman across all three collections in parallel:
   - `secops-api-audit`
   - `api-doc-demo-portal`
   - `tech-support-agent`
3. **Artifact Upload**: Uploads standalone interactive HTML test reports generated with `newman-reporter-htmlextra` as GitHub Actions run artifacts.

## Usage Guidelines

- Use environment variables instead of hardcoding URLs or secrets in requests.[web:38][web:41][web:44]
- Keep collections focused per service or bounded context.
- Prefer descriptive request and folder names over IDs.[web:40]
- Update examples when API responses change to keep documentation accurate.[web:34][web:42]
- Share a link to this repository alongside API docs so other developers can quickly import the collections.[web:39]

## Roadmap

- Add more collections for new services and endpoints.
- Add data-driven tests using CSV/JSON runners.
- [x] Add Newman-based GitHub Actions CI matrix workflow.
- [x] Generate visual HTML reports from Newman runs with `newman-reporter-htmlextra`.
- Add contract-style tests for critical endpoints.

## License

Choose a license that fits your intended use, such as MIT, Apache-2.0, or a private internal license.
