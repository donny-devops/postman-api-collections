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
│   ├── service-a.postman_collection.json
│   ├── service-b.postman_collection.json
│   └── ...
├── environments/
│   ├── local.postman_environment.json
│   ├── dev.postman_environment.json
│   ├── staging.postman_environment.json
│   └── prod.postman_environment.json
└── scripts/
    └── newman-run-examples.sh
```

> Adjust file names to match your actual services and environments.

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

## Running Collections with Newman

You can run these collections in CI/CD or locally using **Newman**, Postman’s CLI runner.

### Install Newman

```bash
npm install -g newman
```

### Basic Run

```bash
newman run collections/service-a.postman_collection.json \
  -e environments/dev.postman_environment.json
```

### Example CI-friendly command

```bash
newman run collections/service-a.postman_collection.json \
  -e environments/staging.postman_environment.json \
  --reporters cli,junit \
  --reporter-junit-export reports/service-a-junit.xml
```

You can place common Newman commands or scripts in the `scripts/` directory for reuse in pipelines.

## Usage Guidelines

- Use environment variables instead of hardcoding URLs or secrets in requests.[web:38][web:41][web:44]
- Keep collections focused per service or bounded context.
- Prefer descriptive request and folder names over IDs.[web:40]
- Update examples when API responses change to keep documentation accurate.[web:34][web:42]
- Share a link to this repository alongside API docs so other developers can quickly import the collections.[web:39]

## Roadmap

- Add more collections for new services and endpoints.
- Add data-driven tests using CSV/JSON runners.
- Add Newman-based GitHub Actions / CI templates.
- Add contract-style tests for critical endpoints.
- Generate HTML reports from Newman runs.

## License

Choose a license that fits your intended use, such as MIT, Apache-2.0, or a private internal license.
