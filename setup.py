import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "SPELLING-CORRECTION-PROJECT"
AUTHOR = "Pham Nguyen Khanh Minh"
SRC_REPO = "spelling"
AUTHOR_EMAIL = "20120117@student.hcmus.edu.vn"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Đồ án ngôn ngữ học tính toán - Spelling Correction - HCMUS ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https:://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https:://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=  setuptools.find_packages(where="src")
)