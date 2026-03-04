# 🔗 API Design Contracts

## 🎯 Purpose of API Contracts

API contracts define the shape of requests and responses for each endpoint in a consistent, machine-validated way.

They serve as:

- 📖 `Documentation` for developers integrating with the API.

- ✅ `Validation` to ensure clients and servers agree on input/output.

- 🛡️ `Governance` to enforce consistent error handling and payload formats across services.

By storing contracts as `JSON` and validating them against a shared `schema`, we prevent drift between implementation and design.

## 🗂️ JSON Schema Structure

All contracts are validated against a single schema (`schema.json`).

It enforces:

- 📌 Presence of required fields (`endpoint`, `method`, `request`, `responses`).

- 🔢 Standardized HTTP status codes and descriptions.

- 🧩 Consistent data types for request params, body, and response examples.

This allows contracts to evolve while staying predictable and compatible.

## 📦 Common Response Format

Every response follows a standard structure for consistency across endpoints:

```json
{
    "status": "success | error",
    "message": "string (optional, required if error)",
    "data": "T (object, array, or null)"
}

```

- 🟢 `status`: Indicates outcome (success or error).

- 💬 `message`: Provides context, required when status = error.

- 📊 `data`: Holds payload or is null if none applies.

## 🛠️ Example Contracts (GET, POST, PUT, DELETE)

Contracts are stored as JSON files in contracts/ (e.g., clients.json) with example responses in examples/{model}/{verb}.{status}.json.


- 📥 `GET` /api/clients/:id → Retrieve a client.

- ➕ `POST` /api/clients → Create a new client.

- ✏️ `PUT` /api/clients/:id → Update an existing client.

- ❌ `DELETE` /api/clients/:id → Remove a client.

Each contract defines:

- 🧾 Request format (params, body).

- 📑 Possible responses with examples (200, 400, 404, etc).

- ♻️ Reusable errors (`errors.json`) to avoid duplication.

## 🧪 How to Validate Locally

Contracts can be validated against the schema before pushing changes.

```bash
make validate-api-design

```

This runs validate_contracts.py which:

- 📂 Loads `schema.json`.

- 🔍 Validates all `*.json` files in `server/api_design/contracts`.

- 🟢 Reports success ✅ or detailed validation errors ❌.

## 🔄 CI Enforcement of Contract Validation

To ensure consistency, contract validation runs automatically in CI/CD (GitHub Actions):

```yaml
- name: Validate API design contracts
  run: make validate-api-design

```

This prevents merging contracts that break schema rules or introduce inconsistencies.s