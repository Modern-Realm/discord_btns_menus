import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycord-btns-menus",
    version="0.2.3",
    author="P. Sai Keerthan Reddy",
    author_email="saikeerthan.keerthan.9@gmail.com",
    description="A responsive package for Buttons, DropMenus, Combinations and Paginator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skrphenix/pycord_btns_menus",
    project_urls={
        "Documentation": "https://skrphenix.github.io/pycord_btns_menus/",
        "Bug Tracker": "https://github.com/skrphenix/pycord_btns_menus/issues",
        "Examples": "https://github.com/skrphenix/pycord_btns_menus/tree/main/Examples",
        "Source": "https://github.com/skrphenix/pycord_btns_menus/tree/main/package/btns_menus",
        "Support Server": "https://discord.gg/GVMWx5EaAN",
    },
    keywords=["pycord", "py-cord", "btns", "pycord buttons",
              "pycord btns", "pycord btns menus", "py-cord btns menus"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    license="MIT",
    package_dir={"": "package"},
    packages=["btns_menus", "btns_menus.builds"],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "py-cord @ git+https://github.com/Pycord-Development/pycord"
    ]
)
