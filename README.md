SeleniumHandler
===============

A class for interacting with web pages using Selenium WebDriver.

 # Usage
   ```

        <!-- Import the service -->
        from sel_service import SeleniumHandler
        
        <!-- Reference to chrome driver exe location -->
        CHROME_DRIVER_PATH = "chromedriver.exe"

        <!-- Initialize the service -->
        handler= SeleniumHandler(CHROME_DRIVER_PATH)

        <!-- Start and navigate to URL -->
        handler.start_driver()
        handler.navigate_to_url("https://www.youtube.com/")



        <!-- Use methods -->
        page_content= handler.scrape_page_content()
        print(page_content)

        links = handler.collect_all_links()
        print(links)
        time.sleep(600)

        handler.stop_driver()
```

Initialization
---------------

code-block: python

    SeleniumHandler(driver_path)

    Parameters:
        - driver_path (str): The file path to the ChromeDriver executable.

Methods
-------

- ``start_driver()``
    Start the WebDriver session with the specified ChromeDriver.

- ``stop_driver()``
    Stop the WebDriver session.

- ``navigate_to_url(url)``
    Navigate the browser to the specified URL.

- ``fill_form_field(field_type, field_name, value)``
    Fill a form field with the specified value.

- ``find_element(locator_type, locator_value, timeout=10)``
    Find an element on the page using the specified locator.

- ``scrape_page_content()``
    Extract the text content of the entire page.

- ``collect_all_links(timeout=10)``
    Collect all links on the page.

Details
-------

- ``start_driver()``
    Initializes the WebDriver session using the specified ChromeDriver executable.
    If successful, prints "Browser started successfully." Otherwise, prints an error message.

    Example::

        handler = SeleniumHandler(driver_path)
        handler.start_driver()

- ``stop_driver()``
    Stops the current WebDriver session.
    If successful, prints "Browser stopped." Otherwise, prints "Browser is not running."

    Example::

        handler.stop_driver()

- ``navigate_to_url(url)``
    Navigates the browser to the specified URL.
    If successful, prints "Browser navigated to URL: {url}". Otherwise, prints an error message.

    Example::

        handler.navigate_to_url("https://www.example.com")

- ``fill_form_field(field_type, field_name, value)``
    Fills a form field with the specified value.
    Parameters:
        - field_type (str): Type of the form field (e.g., 'name', 'id').
        - field_name (str): Name or ID of the form field.
        - value (str): Value to fill in the form field.
    If successful, prints "Filled {field_type} field '{field_name}' with value '{value}'". Otherwise, prints an error message.

    Example::

        handler.fill_form_field("id", "username", "exampleuser")

- ``find_element(locator_type, locator_value, timeout=10)``
    Finds an element on the page using the specified locator.
    Parameters:
        - locator_type (str): Type of locator (e.g., 'id', 'class_name', 'xpath').
        - locator_value (str): Value of the locator.
        - timeout (int, optional): Maximum time to wait for the element to be located (in seconds). Defaults to 10.
    Returns:
        - WebElement: The found WebElement or None if the element is not found.

    Example::

        element = handler.find_element("id", "submit_button")

- ``scrape_page_content()``
    Extracts the text content of the entire page.
    Returns:
        - str: The text content of the page.

    Example::

        page_content = handler.scrape_page_content()

- ``collect_all_links(timeout=10)``
    Collects all links on the page.
    Parameters:
        - timeout (int, optional): Maximum time to wait for the links to be collected (in seconds). Defaults to 10.
    Returns:
        - list: A list of URLs found on the page.

    Example::

        links = handler.collect_all_links()

        


  