# Python CI/CD Pipeline

This project demonstrates a continuous integration and simulated deployment pipeline for a small Python application. Every push triggers one unit test, one headless Selenium UI test, and a deployment confirmation step in GitHub Actions.

## Project structure

```text
.
|-- .github/workflows/ci-cd.yml
|-- app.py
|-- test_unit.py
|-- test_ui.py
|-- requirements.txt
`-- README.md
```

## What the pipeline does

1. Checks out the repository.
2. Sets up Python 3.12 and caches pip dependencies.
3. Installs pytest and Selenium.
4. Runs exactly one unit test for the telecom-tax function.
5. Runs exactly one headless Chrome test against `https://example.com`.
6. Prints `All tests passed! Application successfully deployed to production.` only after both tests pass.

## Run locally

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the unit test:

```powershell
python -m pytest test_unit.py -v
```

Run the Selenium UI test:

```powershell
python -m pytest test_ui.py -v
```

Run both tests:

```powershell
python -m pytest -v
```

## Test coverage

- Unit test: verifies that applying a 10% telecom tax to 100 produces 110.
- UI test: launches Chrome in headless mode, opens Example Domain, and verifies the page title.

The deployment stage is intentionally simulated by printing the required confirmation message after all tests succeed.
