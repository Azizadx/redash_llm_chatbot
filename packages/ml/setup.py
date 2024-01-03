import setuptools


__version__ = "0.0.1"

REPO_NAME = "redash_llm_chatbot"
AUTHOR_USER_NAME = "azizadx"
SRC_REPO = "redash_llm_chatbot"
AUTHOR_EMAIL = "craft@azizadx.me"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Redash LLM Chatbot: AI-powered Analytics &amp; Insights Unlock the power of your Redash dashboards and databases with natural language queries and automated insights.",
    # long_description='Redash LLM Chatbot: AI-powered Analytics &amp; Insights Unlock the power of your Redash dashboards and databases with natural language queries and automated insights.',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
