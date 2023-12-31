## Configuration for this package

### Creating a Virtual Environment

#### Using Conda 🐍

If you prefer Conda as your package manager:

1. Open your terminal or command prompt.
2. Navigate to packages/data_scraper folder.
3. Run the following command to create a new Conda environment:

   ```bash
   conda create --name your bs python=3.11.5
    ```
    The name `bs` stand for data_scraper which use this version of python `3.11.5`.

4. Activate the environment:

    ```bash
    conda activate bs
    ```

#### Using Virtualenv

If you prefer using `venv`, Python's built-in virtual environment module:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new virtual environment:

    ```bash
    python -m venv bs
    ```

    `bs` it  Stand for data_scraper .

4. Activate the environment:

    - On Windows:

    ```bash
    .\bs\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source bs/bin/activate
    ```

### Install the required dependencies inside the data_scraper:
    ```bash
    pip install -r requirements.txt
    ```
### Create the .env file inside the folder package/data_scraper
    ```bash
    touch .env
    ```
    the details content for this file will be shared in slack group with authorized individuals only
