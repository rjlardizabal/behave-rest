# behave-rest

BDD-style Rest API testing tool

It uses python's [requests](https://pypi.python.org/pypi/requests/) for performing HTTP requests, [nose](https://pypi.python.org/pypi/nose/1.3.7) for most assertions, [trafaret](https://github.com/Deepwalker/trafaret) for json validation and [behave](https://pypi.python.org/pypi/behave/1.2.5) for BDD style of tests.

## Installation
Run `pip install behave_rest` to download package and install required dependencies

OR

Clone project

Run `pip install -r requirements.txt` to install required dependencies

## Running

```bash
# to execute all feature files (all tests)
behave

# to execture specific feature
behave features/restapitest.feature

# to see printed output add --no-capture
behave --no-capture

# run features with specific tags
behave --tags=restapiexample --tags=slow

```
More about behave tool you can read here https://pythonhosted.org/behave/index.html

## CI reports
Behave support JUnit reports, that are easily parsed by CI tools

To enable HTML reports, create `behave.ini` file:
```
[behave.formatters]
html = behave_html_formatter:HTMLFormatter
```

```bash
# To run test with report 
behave -f html -o behave-report.html
```

## SSL validation

By default, `requests` has a turned on SSL validation. This can be turned off globally, by setting `context.verify_ssl = True` in `environment.py`, or by using steps described in [Wiki page](https://github.com/stanfy/behave-rest/wiki#steps-related-to-ssl-validation) 

## Project Structure

Feature files are intended to locate in `/features` folder

Corresponding steps are located in `/features/steps`

Overall project structure is as follows:

```
+-- requirements.txt // store python requirements

+-- behave_rest/
    
    +-- environment.py // contains common actions related to scenarios (e.g. clearting headers after running each feature file)

    +-- steps/

        +-- __init__.py // contains common steps definitions

+-- features/

    +-- conf.yaml // store project config (urls, global variables, etc.)

    +-- environment.py // context setup steps (e.g. load from config)

    +-- *.feature // feature files

    +-- steps/

        +-- __init__.py // used to import predefined steps

        +-- json_responses.py // response structures described in Trafaret format

        +-- *.py // steps related to corresponding feature (e.g. "login.py" contains steps that are related to "login.feature")  
        
```
